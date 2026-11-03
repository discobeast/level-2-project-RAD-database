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


#===========================================================
# App Routes Handlers
#===========================================================

#Helper function to redirect with HTMX
#HTMX redirect is smoother than form (Normal) redirect and allows HTMX functions to finish before redirect
def hx_redirect(url):
    resp = make_response()
    resp.headers['HX-Redirect'] = url
    return resp

def make_device_active(id,db):
    query = "UPDATE computers SET condition = 'In Progress' WHERE id = ? AND condition = 'Not started';"
    args = (id,)
    if db.execute(query,args).rowcount > 0:
        resp =  make_response()
        resp.headers["HX-Trigger"] = "update_condition"
    else:
        resp = ""
    return resp

#Render the main page
@app.route("/", methods=['GET','POST']) 
def index():
    return render_template("pages/dashboard.jinja")

#The device list
@app.post("/devices/")
def devices():

    unloved = True if request.form.get('filter_unloved') else False

    bricked = True if request.form.get('filter_bricked') else False

    #In the case that term is somehow NONE term is blank
    term = f"%{request.form['query']}%"
    if not term:
        term = "%%"
    with connect_db() as db:
        query = f"""
                    SELECT computers.id, computers.model, MAX(work_done.timestamp) AS timestamp, work_done.user AS last_user FROM computers 
                    LEFT JOIN work_done ON computers.id = work_done.computer 
                    WHERE (computers.id LIKE ? OR computers.model LIKE ? OR last_user LIKE ?) {"AND timestamp IS NULL" if unloved else ""}
                    GROUP BY computers.id, computers.model 
                    ORDER BY timestamp DESC
                """
        devices = db.execute(query,(term,term,term)).fetchall()

    #if there is only one valid device, assume the user wants to visit that device's page and redirect
    if len(devices) == 1:
        return hx_redirect(url_for('device_page',id=devices[0]["id"]))
    else:
    #Otherwise just render the valid devices
        return render_template("partials/device_list.jinja",devices=devices)

#The per device page
@app.route("/devices/<id>", methods=['GET','POST'])
def device_page(id):
    with connect_db() as db:
        #Get the device information
        query = "SELECT computers.id, computers.model, computers.condition FROM computers WHERE computers.id = ?"
        args = (id,)
        device = db.execute(query,args).fetchone()

        #get the checklist entries associated with this device
        query = """
            SELECT 
                checks.name as name,
                checks.id as id,
                status.outcome as status,
                status.notes as note

            FROM checks
            LEFT JOIN status ON checks.id = status.`check` AND status.computer = ?;
        """
        device['checks'] = db.execute(query,args).fetchall()

        #Get the log entries associated with this device
        query = "SELECT user,notes,timestamp FROM work_done WHERE computer = ?;"
        device['worklogs'] = db.execute(query,args).fetchall()

        return render_template("pages/device.jinja", device=device)

#Post to update a device's checklist entries
@app.post("/devices/<id>/checklist")
def device_update_checklist(id):
    with connect_db() as db:
        #Get all the possible checks
        checks = db.execute("SELECT checks.id FROM checks").fetchall()

        data = request.form
        args = []
        values = ""
        #For every check, upsert the values to the database
        for check in checks:
            check = check['id']
            note = data.get(f"{check}-notes","").strip()
            #Check if the form returned anything about the check being turned on (Because this archaic form system apparently returns "on" or literally nothing to indicate whether an input is checked)
            state = 1 if data.get(f"{check}-check_passed") == 'on' else 0

            #append all the args to the args list
            args.append(id)
            args.append(state)
            args.append(note)
            args.append(check)

            #append the query with the placeholders
            if check != len(checks):
                values += "(?,?,?,?),"
            else:
                values += "(?,?,?,?)"

        #Upsert query, if there is already an entry overwrite it else create entry
        query = f"""INSERT INTO status (computer,outcome,notes,"check")
                    VALUES {values} ON CONFLICT (computer, "check")
                    DO UPDATE SET outcome = excluded.outcome, 
                    notes = excluded.notes"""
        db.execute(query,tuple(args))

        #Return nothing because we dont want the form to redirect the user
        return make_device_active(id,db)

#add something to the worklogs
@app.route("/devices/<id>/worklog",methods=["GET","POST"])
def device_update_worklog(id):

    #if its a post, assume we are making a new entry for the device
    if request.method == "POST":
        with connect_db() as db:
            name = request.form['name']
            notes = request.form['notes']
            query = """INSERT INTO work_done (computer,user,notes) VALUES (?,?,?);"""
            args = (id,name,notes)
            db.execute(query,args)
        return make_device_active(id,db) #Again, return nothing because we dont want the page to refresh (Anything that needs to update refreshes automatically)

    #Assume we are trying to render the log entries for this device
    else:
        with connect_db() as db:
            worklog = db.execute("SELECT user,notes,timestamp FROM work_done WHERE computer = ?;",(id,)).fetchall()
        return render_template("partials/logs.jinja",worklogs = worklog)

#Creation of a new device
@app.post("/devices/new")
def new_device():
    with connect_db() as db:
        id = request.form['id'].strip()
        model = request.form['model'].strip()
        if not id or not model: #We require an ID as otherwise it's generated device page address would link to /devices/ which does not exist. Model is technically optional but its nice to have it
            return render_template('partials/form.jinja',message="ID and Model are required fields.",status="error",id=id,model=model) #Return partial with an error if they omitted ID or model
        
        query = "SELECT computers.id FROM computers WHERE computers.id = ?;" #Check if a device exists with the same ID
        args = (id,)
        if not db.execute(query,args).fetchall(): #If the return is empty then we continue (Empty objects are considered False by Python)
            query = "INSERT INTO computers (id,model) VALUES (?,?);"
            vars = (id,model)
            db.execute(query,vars)
            return hx_redirect(url_for('device_page',id = id))
        else:
            return render_template('partials/form.jinja',message="Device with this ID already exists.",status="error",id=id,model=model) #Return partial with error if a device with that ID already exists


#trying to delete a device
@app.get("/devices/<id>/delete")
def delete_device(id):
    if request.args.get("confirmed", False): #Make sure the user cant somehow accidentally type /devices/.../delete and remove a device
        query = "DELETE FROM computers WHERE computers.id = ?;"
        args = (id,)
        with connect_db() as db:
            db.execute(query,args)
        resp = make_response()
        resp.headers['HX-Redirect'] = "/"
        return resp
    else:
        return render_template('partials/delete.jinja',id=id ) #IF the user somehow typed /devices/.../delete then show a blank page with just a yes/no button to confirm
        #If the user somehow types /devices/.../delete?confirmed=true there is no helping them.
    
@app.post("/devices/<id>/condition")
def update_condition(id):
    condition = request.form.get("condition")
    print(bool(condition in ["Not started", "In Progress", "Completed", "Bricked"]))
    if condition in ["Not started", "In Progress", "Completed", "Bricked"]:
        with connect_db() as db:
            query = "UPDATE computers SET condition = ? WHERE id = ?"
            args = (condition,id)
            db.execute(query,args)
        return render_template('partials/condition.jinja', id=id, condition=condition)
    else:
        with connect_db() as db:
            query = "SELECT condition FROM computers WHERE id = ?"
            args = (id,)
            condition = db.execute(query,args).fetchone()["condition"]
        return render_template('partials/condition.jinja', id=id, condition=condition)

    

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

