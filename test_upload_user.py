import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *


config = config()
base = config['API']['base_url']
username = "UssopSama"
url = f"{base}{user.get_user_by_name}"
json = {
  "id": 0,
  "username": "UssopSama2",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}

def test_upload_user():
    with allure.step("upload an user"):
        response = requests.put(url.format(username=username), json=json)

        assert response.status_code == 200

        body = response.json()
        print_json(data=body)

        allure.attach(response.text, "response API")
        allure.attach(str(response.status_code), "Code HTTP")
