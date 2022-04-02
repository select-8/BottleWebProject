"""
Routes for the bottle application.
"""

from bottle import route, view, redirect, template, request, HTTPError
from bottle import post, get, put, delete
import json
import sqlite3

#helper functions
def zipper(rows,headers):

    # zip headers and rows and add to list
    zipped_data = []
    for r in rows:
        zipped = zip(headers,r)
        zipped_data.append(list(zipped))

    # convert tuples to a dictionary
    zipped_data_as_dict = []
    for r in zipped_data:
        tups_to_dict = {key: value for key, value in r}
        zipped_data_as_dict.append(tups_to_dict)

    return zipped_data_as_dict


@route('/')
def hello():
    """Renders a sample page."""
    redirect('/show/table')


@route('/show/<view>', method='GET')
def showall(view,db):

    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    rows = c.execute('SELECT * from points').fetchall()
    columns = c.execute('PRAGMA table_info(points);').fetchall()
    
    headers = []

    for c in columns:
        headers.append(c[1])

    table_data = zipper(rows,headers)

    if rows:
        if view == 'table':
            output = template('show', table_data=table_data, columns=columns)
        elif view == 'raw':
            output = json.dumps(rows)
        else:
            output = HTTPError(404, "Page not found")
        return output

    if request.forms.get('newdata'):
        redirect("/new")


@route('/new')
def add_new():
    return template('add_data')


@route('/new', method='POST')
def add_new():
    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    city = request.forms.get('newcity')
    colour = request.forms.get('newcolour')
    c.execute('INSERT INTO points (Name,Colour) VALUES(?,?)', (city,colour))
    conn.commit()
    redirect("/")
    c.close()


@route('/update', method='POST')
def update_row():
    data = request.forms.get('nnn')
    print('DATA', data)
    redirect("/")


@post('/add_item_button')
def goadd():

    if request.forms.get('newdata'):
        redirect("/new")


@post('/get_row_to_edit',is_xhr=True)
def goedit():

    id = json.load(request.body)
    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    query = "SELECT * FROM points WHERE ID = {}".format(id)
    data_to_edit = c.execute(query).fetchall()
    conn.commit()
    redirect("/edit_the_row/{}".format(data_to_edit[0]))


from ast import literal_eval
@route('/edit_the_row/<data>')
def open_edit_form(data):
    data_in_a_list = list(literal_eval(data))
    if data_in_a_list:
        return template('edit', data_in_a_list=data)
        

# @route('/time_to_edit/<data>')
# def getediting(data):
#     return template('edit', data_in_a_list=data)


@post('/mapdata',is_xhr=True)
def get_map_data():

    geog = json.load(request.body)

    return geog