
import json
import requests

#POST


def test_create_user():

    point = 'https://petstore.swagger.io/v2/user'
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"
               }
    body = {
        "id": 0,
        "username": "Vasia_2",
        "firstName": "Harry",
        "lastName": "Potter",
        "email": "pottergmail.com",
        "password": "ice cream123",
        "phone": "2345655",
        "userStatus": 0
    }
    booking_json = json.dumps(body)
    response = requests.post(point, data=booking_json,headers=headers)
    assert response.status_code == 200
    print(response.content)

#PUT


def test_update_user():
    point = 'https://petstore.swagger.io/v2/user/vasia'
    headers = {"Content-Type": "application/json",
               "Accept": "application/json"}
    body = {
        "id": 0,
        "username": "rrrrr",
        "firstName": "Harry",
        "lastName": "Potter",
        "email": "pottergmail.com",
        "password": "ice cream123",
        "phone": "2345655",
        "userStatus": 0}
    updated_booking_json = json.dumps(body)
    response = requests.put(point, data=updated_booking_json, headers=headers)
    assert response.status_code == 200
    print(response.content)


#GET

def test_get_user():
    point = 'https://petstore.swagger.io/v2/user/Vasia_2'
    headers = {"Accept": "application/json"}
    response = requests.get(url=point, headers=headers)
    print(response.content)
    assert response.status_code == 200


#DELETE

def test_delete_user():
    point = 'https://petstore.swagger.io/v2/user/Vasia_2'
    headers = {"Accept": "application/json"}
    response = requests.delete(url=point,headers=headers)
    assert response.status_code == 200





