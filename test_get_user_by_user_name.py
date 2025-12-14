import allure
import requests
from utilities.ressources import *
from utilities.configuration import *


config = config()
base = config['API']['base_url']
username = "UssopSama3"
url = f"{base}{user.get_user_by_name.format(username=username)}"

def test_get_user_by_user_name():
    with allure.step('get user by username'):
        requests.get(url)

