import allure
import requests
from rich import print_json
from utilities.configuration import *
from utilities.ressources import *

config = config()
base = config['API']['base_url']
url = f"{base}{user.user_login}"

username = "UssopSama3"

def test_get_logs_user_into_the_system():
    with allure.step('logs user into the system'):
        response = requests.get(url,
                                params={"username" : username,
                                        "password": "123456"}
        )

        assert response.status_code == 200

        allure.attach(str(response.status_code), "CODE HTTP")
        allure.attach(response.text, "API response")

        body = response.json()
        print_json(data=body)

