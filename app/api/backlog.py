import os
from dotenv import dotenv_values
import requests

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
config = dotenv_values(dotenv_path)


def fetch_backlogs(id):
    response = requests.get(f"{config['BASE_URL']}/backlogs/{id}")
    return response.json()

def create_backlog(data):
    response = requests.post(f"{config['BASE_URL']}/backlogs", json=data)
    return response.json()

def update_backlog(id, data):
    response = requests.put(f"{config['BASE_URL']}/backlogs/{id}", json=data)
    return response.json()

def delete_backlog(id):
    response = requests.delete(f"{config['BASE_URL']}/backlogs/{id}")
    return response.json()