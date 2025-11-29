import allure
import requests
from rich import print_json
from utilities.configuration import *
from utilities.ressources import *

config = config()
base_url = config['API']['base_url']
username = "UssopSama"
url = f"{base_url}{user.get_user_by_name.format(username=username)}"


def test_get_user_by_userName():
    with allure.step("get user by user name"):
        response = requests.get(url)

        assert response.status_code == 200

        allure.attach(response.text, "API response")
        allure.attach(str(response.status_code), 'HTTP Code')

        body = response.json()
        print_json(data=body)

