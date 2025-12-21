import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *


config = config()
base = config['API']['base_url']
url = f"{base}{user.user_login}"
params = {'username': "UssopSama3",
          'password': "string"}

def test_get_user_into_the_system():
    with allure.step("logs user to the system"):
        response = requests.get(url, params= params)

        assert response.status_code == 200

        allure.attach(str(response.status_code), "Code HTTP")
        allure.attach(response.text, "API response")

        body = response.json()
        print_json(data=body)

