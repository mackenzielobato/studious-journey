from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)

office_path = './offices.csv'

@app.route("/")
def home():
    return "Hello World!", 200  


class Offices(Resource):
    def get(self):
        office_data = pd.read_csv(office_path)
        office_data = office_data.to_dict()
        return {'office data': office_data}, 200

api.add_resource(Offices, '/offices')

if __name__ == '__main__':
    app.run(debug=True)  # run flask app