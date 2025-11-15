import allure
import requests
from utilities.ressources import *
from utilities.configuration import *


cfg = config()
base = cfg['API']['base_url']
url = f"{base}{apiRessources.statusPet}"
status = 'sold'

def test_find_a_pet_by_status():
    with allure.step('Appel GET / get pet by status'):
        response = requests.get(url,  params={"status": status})

        allure.attach(str(response.status_code), name='Code HTTP')
        allure.attach(response.text, name='Response API')

        assert response.status_code == 200

        print(response.status_code)
        print(response.text)