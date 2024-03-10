from flask import Flask
from flask_sock import Sock
from marshmallow import Schema, fields, validates, ValidationError
import json
import uuid 

CANDIDATE_DATA_FILE = "candidates_data.json"
app = Flask(__name__)
sock = Sock(app)


def load_data():
    try:
        with open(CANDIDATE_DATA_FILE, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

candidatesData = load_data()

def save_data(data):
    with open(CANDIDATE_DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def add_data(new_data):
    data = load_data()
    new_data['id'] = str(uuid.uuid4())  # Generate a UUID as the ID
    data.append(new_data)
    save_data(data)
    return new_data['id']

def update_data(id, updated_data):
    data = load_data()
    for item in data:
        if item['id'] == id:
            item.update(updated_data)
            break
    save_data(data)

@sock.route('/addCandidate')
def addCandidate(ws):
    while True:
        message_data = ws.receive()
        
        # Deserialize the received message using MessageSchema
        try:
            message = CandidateSchema().load(message_data)
            id = add_data(message)
            ws.send("Candidate Added successfully with ID: " + id)

        except Exception as e:
            print("Error deserializing message:", e)
            continue

@sock.route('/updateCandidateData')
def updateCandidateData(ws):
    while True:
        message_data = ws.receive()
        
        # Deserialize the received message using MessageSchema
        try:
            message = UpdateCandidateDataSchema().load(message_data)
            id = message.id
            update_data = message.update_data
            update_data(id, update_data)
            ws.send("Candiate" +id+  "updated successfully")
        except Exception as e:
            print("Error deserializing message:", e)
            continue

@sock.route('/refreshData')
def refresh_data(ws):
    # Logic to retrieve all candidate data from the database
    candidates = load_data()
    candidatesData = candidates
    # Emit all candidate data to connected clients
    ws.send(candidatesData)





class UpdateCandidateDataSchema(Schema):
    id = fields.Str(required=True)
    first_name = fields.Str(required=False)
    last_name = fields.Str(required=False)
    age = fields.Int(required=False, validate=lambda x: x > 0)  # Age should be a positive integer
    experience_years = fields.Float(required=False, validate=lambda x: x >= 0)  # Experience in years, non-negative
    linkedin_url = fields.URL(required=False, validate=lambda x: x.startswith('https://www.linkedin.com/'))  # Validate URL format
    availability = fields.Str(required=False)  # You can customize validation for availability, e.g., choices=['Full-time', 'Part-time', 'Contract']
    
class CandidateSchema(Schema):
    id = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    age = fields.Int(required=True, validate=lambda x: x > 0)  # Age should be a positive integer
    experience_years = fields.Float(required=True, validate=lambda x: x >= 0)  # Experience in years, non-negative
    linkedin_url = fields.URL(required=True, validate=lambda x: x.startswith('https://www.linkedin.com/'))  # Validate URL format
    availability = fields.Str(required=True)  # You can customize validation for availability, e.g., choices=['Full-time', 'Part-time', 'Contract']
    
   