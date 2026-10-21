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
    if request.method == "GET":
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
            args = (id,)
            checks = db.execute(query,args).fetchall()
            device['checks']=checks

            return render_template("pages/device.jinja", device=device)
    elif request.method == "POST":
        with connect_db() as db:
            checks = db.execute("SELECT checks.id FROM checks").fetchall()
            data = request.form
            args = []
            values = ""
            for check in checks:
                check = check['id']
                note = request.form.get(f"{check}-notes","")
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

# @app.route("/devices/<id>/checklist/<check>", methods=['GET','POST'])
# def device_checklist(id,check):
#     if requeq
#     return render_template("partials/check.jinja")



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

