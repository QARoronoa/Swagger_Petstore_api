import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *


cfg = config()
base = cfg['API']['base_url']
url = f"{base}{user.get_user_by_name}"
username = "UssopSama3"


def test_delete_user_by_username():
    with allure.step("delete user by username"):
        response = requests.delete(url.format(username=username))

        assert response.status_code == 200
        body = response.json()

        print_json(data=body)

        allure.attach(str(response.status_code), "CODE HTTP")
        allure.attach(response.text, "RESPONSE API")

