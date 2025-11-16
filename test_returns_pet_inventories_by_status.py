import allure
import requests
from utilities.ressources import *
from utilities.configuration import *
from rich import print_json

config = config()
base = config['API']['base_url']
url = f"{base}{apiRessources.storeInventory}"

def test_returns_pet_inventories_by_status():
    with allure.step('Appel GET / Response API'):
        response = requests.get(url)

        responseBody = response.json()
        print_json(data=responseBody)

        assert response.status_code == 200
        # assert responseBody["active"] == 1

        allure.attach(response.text, name= 'Response API')
        allure.attach(str(response.status_code), name= "Code HTTP")