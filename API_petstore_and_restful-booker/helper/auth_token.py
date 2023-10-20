import json
import requests


def get_token():
    BASE_URL = "https://restful-booker.herokuapp.com"
    auth_endpoint = f"{BASE_URL}/auth"
    headers = {"Content-Type": "application/json"}
    auth_data = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(auth_endpoint, json=auth_data, headers=headers, timeout=200)
    return json.loads(response.text)['token']