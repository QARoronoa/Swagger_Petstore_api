import allure
import requests
from utilities.ressources import *
from utilities.configuration import *
from rich import print_json

congig = config()
base = congig['API']['base_url']
url = f"{base}{apiRessources.findpetId}"
petId = 1763236575
name = "LuffySama"
status = "available"

def test_updates_pet_with_form_data():
    with allure.step('Appel POST/ update a pet'):
        response = requests.post(url.format(petId=petId),
                                 data={"name" : name, "status": status})

        allure.attach(str(response.status_code), name='Code HTTP')
        allure.attach(response.text, name='Réponse API')

        responseBody = response.json()
        print_json(data=responseBody)

        assert response.status_code == 200




