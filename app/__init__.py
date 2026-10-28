#===========================================================
# PROJECT NAME HERE
# By YOUR NAME HERE
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


#===========================================================
# App Routes Handlers
#===========================================================

@app.route("/", methods=['GET','POST']) 
def index():
    with connect_db() as db:
        query = """SELECT computers.id, computers.model FROM computers ORDER BY computers.model DESC"""
        devices = db.execute(query).fetchall()
    return render_template("pages/dashboard.jinja",devices=devices)

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
            note = request.form.get(f"{check}-notes","").strip()
            state = 1 if request.form.get(f"{check}-check_passed",0) == 'on' else 0
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
        print(query)
        db.execute(query,tuple(args))
        return redirect(url_for('device_page',id = id))

@app.post("/devices/<id>/worklog")
def device_update_worklog(id):
    with connect_db() as db:
        name = request.form['name']
        notes = request.form['notes']
        query = """INSERT INTO work_done (computer,user,notes,timestamp) VALUES (?,?,?,?);"""
        formatted_time = time.strftime("%d %B %Y %H:%M:%S", time.localtime(time.time()))
        print(formatted_time)
        args = (id,name,notes,formatted_time)
        db.execute(query,args)
    return redirect(url_for('device_page',id = id))

@app.post("/devices/new")
def new_device():
    print("test")
    id = request.form['id']
    model = request.form['model']
    query = "INSERT INTO computers (id,model) VALUES (?,?);"
    vars = (id,model)
    with connect_db() as db:
        db.execute(query,vars)
    return redirect(url_for('device_page',id = id))

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

