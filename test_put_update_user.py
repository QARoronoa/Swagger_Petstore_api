import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *


config = config()
base = config['API']['base_url']
username = "UssopSama3"

url = f"{base}{user.get_user_by_name}"
data = {
  "id": 0,
  "username": username,
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}

def test_updated_user_by_userName():
    with allure.step("update user by name"):
        response = requests.put(url.format(username=username),
                                json=data)

        assert response.status_code == 200

        body = response.json()
        print_json(data=body)

        allure.attach(str(response.status_code), "HTTP CODE")
        allure.attach(response.text, "Response API")