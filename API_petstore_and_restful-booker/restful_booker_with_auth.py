import json
import pytest
import requests
from helper.auth_token import get_token

# Below are examples of tests where authentication is required

BASE_URL = "https://restful-booker.herokuapp.com"


def test_create_booking():
    endpoint = f"{BASE_URL}/booking"
    headers = {'Content-Type': 'application/json'}
    booking_data = {
        "firstname": "luv",
        "lastname": "lu",
        "totalprice": 600,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-05"
        },
        "additionalneeds": "Breakfast"
    }
    booking_json = json.dumps(booking_data)
    response = requests.post(endpoint, data=booking_json, headers=headers)
    assert response.status_code == 200
    assert "bookingid" in response.json()
    print(response.content)


@pytest.mark.token('test need token')
def test_update_booking():
    booking_id = 1958
    endpoint = f"{BASE_URL}/booking/{booking_id}"
    token = f'token={get_token()}'
    headers = {"Content-Type": "application/json",
               "Accept": "application/json",
               "Cookie": token}
    updated_booking_data = {
        "firstname": "vasia",
        "lastname": "pupkin",
        "totalprice": 300,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-02-06",
            "checkout": "2024-02-10"
        },
        "additionalneeds": "Updated Needs"}
    updated_booking_json = json.dumps(updated_booking_data)
    response = requests.put(endpoint, data=updated_booking_json, headers=headers, timeout=200)
    print(response.content)
    assert response.status_code == 200


@pytest.mark.token('test need token')
def test_delete_booking():
    token = f'token={get_token()}'
    headers = {"Content-Type": "application/json",
               "Cookie": token}
    booking_id = 1958
    endpoint = f"{BASE_URL}/booking/{booking_id}"
    response = requests.delete(url=endpoint, headers=headers, timeout=200)
    assert response.status_code == 201
