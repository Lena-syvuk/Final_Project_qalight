
import json
import requests
from data.user_data_petstore_ import user_create_data,user_update_data
from helper.headers_petstore import headers_data


def test_create_user():

    point = 'https://petstore.swagger.io/v2/user'
    headers = headers_data
    body = user_create_data
    booking_json = json.dumps(body)
    response = requests.post(point, data=booking_json,headers=headers)
    assert response.status_code == 200
    print(response.content)


def test_update_user():
    point = 'https://petstore.swagger.io/v2/user/Vasia_2'
    headers = headers_data
    body = user_update_data
    updated_booking_json = json.dumps(body)
    response = requests.put(point, data=updated_booking_json, headers=headers)
    assert response.status_code == 200
    print(response.content)


def test_get_user():
    point = 'https://petstore.swagger.io/v2/user/Lemur'
    headers = headers_data
    response = requests.get(url=point, headers=headers)
    print(response.content)
    assert response.status_code == 200


def test_delete_user():
    point = 'https://petstore.swagger.io/v2/user/Lemur'
    headers = headers_data
    response = requests.delete(url=point,headers=headers)
    assert response.status_code == 200





