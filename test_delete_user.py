import allure
import requests

from utilities.configuration import *
from utilities.ressources import *
from rich import print_json

config = config()
base = config['API']['base_url']
url = f"{base}{user.get_user_by_name}"
username = "UssopSama3"


def test_delete_user():
    with allure.step("delete an user"):
        response = requests.delete(url.format(username=username))

        assert response.status_code == 200

        body = response.json()
        print_json(data=body)

        allure.attach(response.text, name='API response')
        allure.attach(str(response.status_code), name='Code HTTP')