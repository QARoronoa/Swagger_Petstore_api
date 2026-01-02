import allure
import requests
from rich import print_json
from utilities.configuration import *
from utilities.ressources import *


cfg = config()
base = cfg['API']['base_url']
url = f"{base}{user.user_create_list}"
params = [
  {
    "id": 123321323,
    "username": "Ussop",
    "firstName": "Sama",
    "lastName": "OP",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]

def test_create_list_of_user():
  with allure.step('create a list user'):
    response = requests.post(url, json=params)

    assert response.status_code == 200

    body = response.json()
    print_json(data=body)

    allure.attach(response.text, 'Api response')
    allure.attach(str(response.status_code), 'Code HTTP')


