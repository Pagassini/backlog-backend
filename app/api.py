import requests

BASE_URL = "http://localhost:8081/api/v1"

def fetch_users():
    response = requests.get(f"{BASE_URL}/users")
    return response.json()

def create_user(data):
    response = requests.post(f"{BASE_URL}/users", json=data)
    return response.json()

def fetch_backlogs(id):
    response = requests.get(f"{BASE_URL}/backlogs/{id}")
    return response.json()

def create_backlog(data):
    response = requests.post(f"{BASE_URL}/backlogs", json=data)
    return response.json()

def update_backlog(id, data):
    response = requests.put(f"{BASE_URL}/backlogs/{id}", json=data)
    return response.json()

def delete_backlog(id):
    response = requests.delete(f"{BASE_URL}/backlogs/{id}")
    return response.json()