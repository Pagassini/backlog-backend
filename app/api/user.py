import os
from dotenv import dotenv_values
import requests


dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
config = dotenv_values(dotenv_path)

def fetch_users():
    response = requests.get(f"{config['BASE_URL']}/users")
    return response.json()

def create_user(data):
    response = requests.post(f"{config['BASE_URL']}/users", json=data)
    return response.json()

def delete_user(id):
    response = requests.delete(f"{config['BASE_URL']}/users/{id}")
    return response.json()