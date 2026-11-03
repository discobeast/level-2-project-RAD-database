#===========================================================
# Rad database
# By Jesse
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *
import time


# Create the app
app = Flask(__name__)

def formatTime(timestamp):
    return time.strftime("%d/%m/%Y %H:%M:%S", time.localtime(timestamp))
#===========================================================
# App Routes Handlers
#===========================================================

def hx_redirect(url):
    resp = make_response()
    resp.headers['HX-Redirect'] = url
    return resp


@app.route("/", methods=['GET','POST']) 
def index():
    return render_template("pages/dashboard.jinja")

@app.post("/devices/")
def devices():
    term = f"%{request.form['query']}%"
    if not term:
        term = "%%"
    with connect_db() as db:
        query = """SELECT computers.id, computers.model, MAX(work_done.timestamp) AS timestamp, work_done.user AS last_user FROM computers LEFT JOIN work_done ON computers.id = work_done.computer WHERE computers.id LIKE ? OR computers.model LIKE ? OR last_user LIKE ? GROUP BY computers.id, computers.model ORDER BY timestamp DESC"""
        devices = db.execute(query,(term,term,term)).fetchall()
    if len(devices) == 1:
        return hx_redirect(url_for('device_page',id=devices[0]["id"]))
    else:
        return render_template("partials/device_list.jinja",devices=devices)

@app.route("/devices/<id>", methods=['GET','POST'])
def device_page(id):
    with connect_db() as db:
        query = "SELECT computers.id, computers.model FROM computers WHERE computers.id = ?"
        args = (id,)
        device = db.execute(query,args).fetchone()
        query = """
            SELECT 
                checks.name as name,
                checks.id as id,
                status.outcome as status,
                status.notes as note

            FROM checks
            LEFT JOIN status ON checks.id = status.`check` AND status.computer = ?;
        """
        checks = db.execute(query,args).fetchall()
        device['checks']=checks

        query = "SELECT user,notes,timestamp FROM work_done WHERE computer = ?;"
        worklog = db.execute(query,args).fetchall()
            
        device['worklogs'] = worklog
        return render_template("pages/device.jinja", device=device)


@app.post("/devices/<id>/checklist")
def device_update_checklist(id):
    with connect_db() as db:
        checks = db.execute("SELECT checks.id FROM checks").fetchall()
        data = request.form
        args = []
        values = ""
        for check in checks:
            check = check['id']
            note = data.get(f"{check}-notes","").strip()
            state = 1 if data.get(f"{check}-check_passed") == 'on' else 0
            args.append(id)
            args.append(state)
            args.append(note)
            args.append(check)
            if check != len(checks):
                values += "(?,?,?,?),"
            else:
                values += "(?,?,?,?)"

        query = f"""INSERT INTO status (computer,outcome,notes,"check")
                    VALUES {values} ON CONFLICT (computer, "check")
                    DO UPDATE SET outcome = excluded.outcome, 
                    notes = excluded.notes"""
        db.execute(query,tuple(args))
        return make_response("",200)


@app.route("/devices/<id>/worklog",methods=["GET","POST"])
def device_update_worklog(id):
    if request.method == "POST":
        with connect_db() as db:
            name = request.form['name']
            notes = request.form['notes']
            query = """INSERT INTO work_done (computer,user,notes) VALUES (?,?,?);"""
            args = (id,name,notes)
            db.execute(query,args)
        return ""
    else:
        with connect_db() as db:
            worklog = db.execute("SELECT user,notes,timestamp FROM work_done WHERE computer = ?;",(id,)).fetchall()
        return render_template("partials/logs.jinja",worklogs = worklog)


@app.post("/devices/new")
def new_device():
    with connect_db() as db:
        id = request.form['id'].strip()
        model = request.form['model'].strip()
        if not id or not model:
            return render_template('partials/form.jinja',message="ID and Model are required fields.",status="error",id=id,model=model)
        query = "SELECT computers.id FROM computers WHERE computers.id = ?;"
        args = (id,)
        if not db.execute(query,args).fetchall():
            query = "INSERT INTO computers (id,model) VALUES (?,?);"
            vars = (id,model)
            db.execute(query,vars)
            return hx_redirect(url_for('device_page',id = id))
        else:
            return render_template('partials/form.jinja',message="Device with this ID already exists.",status="error",id=id,model=model)


@app.get("/devices/<id>/delete")
def delete_device(id):
    if request.args.get("confirmed", False):
        query = "DELETE FROM computers WHERE computers.id = ?;"
        args = (id,)
        with connect_db() as db:
            db.execute(query,args)
        resp = make_response()
        resp.headers['HX-Redirect'] = "/"
        return resp
    else:
        return render_template('partials/delete.jinja',id=id )
    
    

#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

