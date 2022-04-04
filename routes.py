"""
Routes for the bottle application.
"""

from bottle import route, view, redirect, template, request, HTTPError
from bottle import post, get, put, delete
import json
import sqlite3
import requests

# helper functions
def zipper(rows, headers):

    # zip headers and rows and add to list
    zipped_data = []
    for r in rows:
        zipped = zip(headers, r)
        zipped_data.append(list(zipped))

    # convert tuples to a dictionary
    zipped_data_as_dict = []
    for r in zipped_data:
        tups_to_dict = {key: value for key, value in r}
        zipped_data_as_dict.append(tups_to_dict)

    return zipped_data_as_dict


"""
Redirect from root route to table view
"""


@route("/")
def index():
    redirect("/show/table")


"""
Retrieve all IsVisible data from the db and convert to a dictionary structure.
Then either render to table view, render as json or return 404 if page not found.
"""


@route("/show/<view>")
def showall(view, db):

    try:
        conn = sqlite3.connect("./data/simpledb.db")
        c = conn.cursor()
        rows = c.execute("SELECT * FROM points WHERE IsVisible = 1").fetchall()
        print("")
        for r in rows:
            print("Row: ", r)
        print("")
        columns = c.execute("PRAGMA table_info(points);").fetchall()
    except Exception as Ex:
        print(Ex)

    headers = []

    for c in columns:
        headers.append(c[1])

    # Remove the IsVisible column
    columns = columns[:-1]

    table_data = zipper(rows, headers)

    for td in table_data:
        print("As a Dict:", td)
    print("")
    if rows:
        if view == "table":
            output = template("show", table_data=table_data, columns=columns)
        elif view == "raw":
            output = json.dumps(rows)
        else:
            output = HTTPError(404, "Page not found")
        return output


"""
When the 'Add New Location' is pressed, 
check for the POST response and return the Add Data form
"""


@post("/add_item_button")
def goadd():

    if request.forms.get("newdata"):
        return template("add_data")
    else:
        return HTTPError(404, "Page not found")


"""
Get data POSTed form in the add_data template and insert value to the db.
Redirect back to the root url.
"""


@route("/new", method="POST")
def add_new():

    city = request.forms.get("newCity")
    long = request.forms.get("newLong")
    lat = request.forms.get("newLat")
    count = request.forms.get("newCount")
    colour = request.forms.get("newColour")

    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO points (Name,Long,Lat,Count,Colour,IsVisible) VALUES(?,?,?,?,?,1)",
        (city, long, lat, count, colour),
    )
    conn.commit()
    redirect("/")
    c.close()


"""
When the Edit button is clicked the JS show() function is called
and the row's id value (same as db row's id) is POSTed.
This value is then redirected to the /time_to_edit route.
"""


@post("/get_row_to_edit", is_xhr=True)
def goedit():
    if request:
        id = json.load(request.body)
        redirect("/time_to_edit/{}".format(id))
    else:
        return HTTPError(404, "Page not found")


"""
The db id value has been redirected from the /get_row_to_edit route.
Use the id to select the relevant row from the db.
Pass this data to the edit form.
The edit form is loaded by bottle but url is not (not sure why).
The url is instead called from the JS show() function.
"""


@route("/time_to_edit/<id>")
def itstime(id):

    id_as_int = int(id)
    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    query = "SELECT * FROM points WHERE ID = {}".format(id_as_int)
    data_to_edit = c.execute(query).fetchall()
    conn.commit()

    return template("edit", data_in_a_list=data_to_edit[0])


"""
This route is called when the submit button in the edit form is clicked.
The POSTed form data is used to update the db values for the entry.
Redirect back to thr root url.
"""


@post("/update")
def update_row():
    id = request.forms.get("id")
    editedcount = request.forms.get("editedcount")
    editedcolour = request.forms.get("editedcolour")
    print(id, editedcount, editedcolour)

    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    query = "UPDATE points SET Count = {}, Colour = '{}' WHERE ID = {}".format(
        editedcount, editedcolour, id
    )
    c.execute(query)
    conn.commit()

    redirect("/")


"""
When the Delete button is clicked the JS hide() function is called
and the row's id value (same as db row's id) is POSTed.
This value is used to set IsVisible to False in the db.
The row is no longer selected by showall().
The page is refreshed by the JS hide() function.
"""


@post("/delete", is_xhr=True)
def hide_record():
    id = json.load(request.body)
    print("ID:", id)
    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    query = "UPDATE points SET IsVisible = 0 WHERE ID = {}".format(id)
    print(query)
    c.execute(query)
    conn.commit()


"""
This route is called when the map is clicked.
TODO: Somehow pass this data to the add_data form (probably jQuery)
"""


@post("/mapdata", is_xhr=True)
def get_map_data():

    geog = json.load(request.body)

    return geog
