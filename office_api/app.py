
from flask import Flask,redirect, render_template
from flask_restful import Resource, Api, reqparse
from numpy import char
import pandas as pd
import ast
#import requests
import json

#initializes flask app
app = Flask(__name__)

#initializes flask api
api = Api(app)

#bring in investor office data
office_path = './office_api/offices.csv'

#home page redirects to api entry point
@app.route("/")
def home():
    #return "Hello World!", 200  
    return redirect("/offices", code=302)

#office class api
class Offices(Resource):
    #GETs office data from the csv, converts it to data frame, then to dictionary, and returns it with 200 OK code
    def get(self):
        office_data = pd.read_csv(office_path)
        office_data = office_data.to_dict()
        return {'office data': office_data}, 200
    #POSTs office data if new investor office data needs to be added to the api, returns arguments added with 200 OK code
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('descriptionID', required=False, type=str)
        parser.add_argument('regionID', required=True, type=str)
        parser.add_argument('address1ID', required=True, type=str)
        parser.add_argument('address2ID', required=False, type=str)
        parser.add_argument('cityID', required=True, type=str)
        parser.add_argument('zip_codeID', required=True, type=str)
        parser.add_argument('state_codeID', required=True, type=str)
        parser.add_argument('country_codeID', required=True, type=str)
        parser.add_argument('latituteID', required=False, type=str)
        parser.add_argument('longitudeID', required=False, type=str)

        args = parser.parse_args()

        return {'desc': args['descriptionID']}, 200
        
#adds office class to api
api.add_resource(Offices, '/offices')

# #home page redirects to api entry point
# @app.route('/')
# def home():
#     #return "Hello World!", 200  
#     return {render_template('index.html',name='home')}
#runs flask app
if __name__ == '__main__':
    app.run(debug=True) 