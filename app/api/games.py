import os
from dotenv import dotenv_values
import requests

dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
config = dotenv_values(dotenv_path)

def fetch_games():
    response = requests.get(f"{config['BASE_URL']}/games")
    return response.json()

def create_games(data):
    response = requests.post(f"{config['BASE_URL']}/games", json=data)
    return response.json()

def update_games(id, data):
    response = requests.put(f"{config['BASE_URL']}/games/{id}", json=data)
    return response.json()

def delete_games(id):
    response = requests.delete(f"{config['BASE_URL']}/games/{id}")
    return response.json()

def fetch_games_by_id(id):
    response = requests.get(f"{config['BASE_URL']}/games/{id}")
    return response.json()