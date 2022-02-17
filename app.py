import dbinteractions as dbi
import getpass as gp
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.get('/item')
def list_all_items():
    try:
        items = dbi.list_all_items()
        items_json = json.dumps(items, default=str)
        return Response(items_json, mimetype="application/json", status=200)
    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


@app.post('/item')
def add_new_item():
    try:
        name = request.json['name']
        description = request.json['description']
        quantity = request.json['quantity']
        new_item = dbi.add_new_item(name, description, quantity)
        if(new_item == True):
            item_json = json.dumps(new_item, default=str)
            return Response(item_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)

    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


@app.patch('/item')
def update_item():
    try:
        item_id = request.json['item_id']
        item_id = dbi.update_item(item_id)
        if(item_id == True):
            item_id_json = json.dumps(item_id, default=str)
            return Response(item_id_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)
    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


@app.delete('/item')
def delete_item():
    try:
        item_id = request.json['item_id']
        item_id = dbi.delete_item(item_id)
        if(item_id == True):
            item_id_json = json.dumps(item_id, default=str)
            return Response(item_id_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)

    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


@app.get('/employee')
def get_employee():
    employee = []
    try:
        employee_id = request.args['employee_id']
        employee = dbi.get_employee(employee_id)
        if(employee != None):
            employee_json = json.dumps(employee, default=str)
            return Response(employee_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)
    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


@app.post('/employee')
def add_new_employee():
    new_employee = None
    try:
        name = request.json['name']
        hourly_wage = request.json['hourly_wage']
        new_employee = dbi.add_new_employee(name, hourly_wage)
        if(new_employee != None):
            employee_json = json.dumps(new_employee, default=str)
            return Response(employee_json, mimetype="application/json", status=200)
        else:
            return Response("Please enter valid data", mimetype="plain/text", status=400)

    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


app.run(debug=True)
