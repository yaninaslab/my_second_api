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
        if(new_item == None):
            return Response("Please enter valid data", mimetype="plain/text", status=400)
        else:
            item_json = json.dumps(new_item, default=str)
            return Response(item_json, mimetype="application/json", status=200)

    except:
        print("Something went wrong")
        return Response("Sorry, something is wrong with the service. Please try again later", mimetype="plain/text", status=501)


app.run(debug=True)
