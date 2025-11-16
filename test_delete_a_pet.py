import time

import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *



config = config()
base = config['API']['base_url']
url = f"{base}{apiRessources.findpetId}"
petId = 1763296519


def test_delete_a_pet():
    with allure.step('Appel DELETE / supprimer un pet'):
        response = requests.delete(url.format(petId=petId))

        assert response.status_code == 200

        allure.attach(str(response.status_code), name='Code HTTP')
        allure.attach(response.text, name='Response API')

        print(response.status_code)
        print(response.text)