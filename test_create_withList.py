import allure
import requests
from rich import print_json
from utilities.ressources import *
from  utilities.configuration import *


config = config()
base = config['API']['base_url']
url = f"{base}{user.creat_list_users}"
data = [
  {
    "id": 0,
    "username": "UssopSama3",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]

def test_create_withList():
    with allure.step("create a user with list"):
        response = requests.post(url, json=data)

        assert response.status_code == 200

        allure.attach(response.text, "API response")
        allure.attach(str(response.status_code), "HTTP Code")

        body = response.json()
        print_json(data=body)
