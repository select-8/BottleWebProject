"""
Routes for the bottle application.
"""

from bottle import route, view, redirect, template, request, HTTPError
from bottle import post, get, put, delete
import json
import sqlite3
import requests

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


@route('/show/<view>', method=['GET','POST'])
def showall(view,db):

    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    rows = c.execute('SELECT * FROM points WHERE IsVisible = 1').fetchall()
    # for r in rows:
    #     print('Row: ', r)
    columns = c.execute('PRAGMA table_info(points);').fetchall()
    
    headers = []

    for c in columns:
        headers.append(c[1])

    # Remove the IsVisible column
    columns = columns[:-1]

    table_data = zipper(rows,headers)
    # for td in table_data:
    #     print('As a Dict:', td)

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
    city = request.forms.get('newCity')
    long = request.forms.get('newLong')
    lat = request.forms.get('newLat')
    count = request.forms.get('newCount')
    colour = request.forms.get('newColour')
    c.execute('INSERT INTO points (Name,Long,Lat,Count,Colour,IsVisible) VALUES(?,?,?,?,?,1)', (city,long,lat,count,colour))
    conn.commit()
    redirect("/")
    c.close()


@post('/add_item_button')
def goadd():

    if request.forms.get('newdata'):
        redirect("/new")


@route('/get_row_to_edit',is_xhr=True, method=['GET', 'POST'])
def goedit():
    if request:
        id = json.load(request.body)
        print(id)
        conn = sqlite3.connect("./data/simpledb.db")
        c = conn.cursor()
        query = "SELECT * FROM points WHERE ID = {}".format(id)
        data_to_edit = c.execute(query).fetchall()

        conn.commit()

        redirect("/time_to_edit/{}".format(id))


import ast
@route('/time_to_edit/<id>',is_xhr=False)
def itstime(id):

    the_val = ast.literal_eval(id)

    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    query = "SELECT * FROM points WHERE ID = {}".format(the_val)
    data_to_edit = c.execute(query).fetchall()
    conn.commit()
    #redirect('/time_to_edit/{}'.format(data_to_edit))
    return template('edit', data_in_a_list=data_to_edit[0])



@route('/update', method='POST')
def update_row():
    id = request.forms.get('id')
    editedcount = request.forms.get('editedcount')
    editedcolour = request.forms.get('editedcolour')
    print(id, editedcount, editedcolour)

    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    query = "UPDATE points SET Count = {}, Colour = '{}' WHERE ID = {}".format(editedcount,editedcolour,id)
    # c.execute("UPDATE database SET temp = ?", (new_temp))
    print(query)
    c.execute(query)
    conn.commit()
    redirect("/")


@post('/delete',is_xhr=True)
def hide_record():
    id = json.load(request.body)
    print('ID:', id)
    conn = sqlite3.connect("./data/simpledb.db")
    c = conn.cursor()
    query = "UPDATE points SET IsVisible = 0 WHERE ID = {}".format(id)
    print(query)
    c.execute(query)
    conn.commit()
    redirect("/")


@post('/mapdata',is_xhr=True)
def get_map_data():

    geog = json.load(request.body)

    return geog