import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *

cfg = config()
base = cfg['API']['base_url']
url = f"{base}{user.create_user}"
json = {
  "id": 0,
  "username": "Roronoa",
  "firstName": "zorro",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}

def test_post_create_user():
    with allure.step('Créer un user'):
        response = requests.post(url, json=json)

        assert response.status_code == 200

        body = response.json()
        print_json(data=body)

        allure.attach(str(response.status_code), "code HTTP")
        allure.attach(response.text, "api response")