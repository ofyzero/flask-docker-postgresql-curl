from flask import Flask,  request, jsonify
from flask_sqlalchemy import SQLAlchemy
import json
import psycopg2
from psycopg2 import Error
import logging
import pandas as pd


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)



logger = logging.getLogger(__name__)

class InputData(db.Model):
    __tablename__ = "campaign"
    # "date": "12/01/2020", "slot_id": 123, "device": "desktop", "impressions": 3000
    id = db.Column(db.Integer, primary_key=True)
    slot_id = db.Column(db.Integer,nullable=False)
    date = db.Column(db.DATE, nullable=False)
    device = db.Column(db.String(128), nullable=False)
    impressions = db.Column(db.Integer,nullable=False)

    def __init__(self, slot_id,date,device,impressions):
        self.slot_id = slot_id
        self.date = date
        self.device = device
        self.impressions = impressions

@app.route('/post', methods=['POST'])
def post():
    if request.method == 'POST':
        # get post data
        # if data format is not JSON , raise issue.
        try:
            data = request.get_json(force=True)

        except:
            return "Pls check JSON format.\n"

        # if any of the element missing , raise issue.
        if not data["filter"] or not data["group_by"] or not data["start_time"] or not data["end_time"]:
            return "Missing request element.\n"

        # create a conncetion to postgresql
        connection = psycopg2.connect(user="hello_flask",
                                      password="hello_flask",
                                      host="decide-jsonapi-db-1",
                                      port="5432",
                                      database="hello_flask_dev"
                                      )
        try :

            # get all table from db
            df = pd.read_sql('select * from campaign', con=connection)

            # if there is a filter
            #filter table
            if data["filter"]:
                for column in data["filter"].keys():
                    df = df.loc[df[column].isin(data["filter"][column])]

            # if there is start_time , filter table
            if data["start_time"]:
                df = df[df["date"] >= pd.to_datetime(data["start_time"])]

            # if there is end_time , filter table
            if data["end_time"]:
                df = df[df["date"] <= pd.to_datetime(data["end_time"])]

            # group by table
            # sum impressions
            if data["group_by"]:
                df = df.groupby(data["group_by"])["impressions"].sum()\
                    .reset_index()\
                    .rename(columns={'sum': 'impressions'})

            print(df)

            result = df.to_dict(orient='records')

        except (Exception, Error) as error:
            print("Error while connecting to PostgreSQL", error)


        return jsonify(result)

@app.route('/get', methods=['GET'])
def get():

    if request.method == 'GET':

        return "Really GET Request Processed.\n"

