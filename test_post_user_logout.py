import allure
import requests

from utilities.ressources import *
from utilities.configuration import *
from rich import print_json

cfg = config()
base = cfg['API']['base_url']
url = f"{base}{user.user_logout}"

def test_logout_user():
    with allure.step("logout user"):
        response = requests.get(url)

        assert response.status_code == 200

        body = response.json()
        print_json(data=body)
        allure.attach(str(response.status_code), "code HTTP")
        allure.attach(response.text, "API response")

