import allure
import requests
from utilities.ressources import *
from utilities.configuration import *
from rich import print_json


cfg = config()
base = cfg['API']['base_url']
url = f"{base}{apiRessources.findpetId}"
petId = 1763233507


def test_find_pet_by_iD():
    with allure.step('Appel GET / find pet by iD'):
        response = requests.get(url.format(petId=petId), timeout=20)

    allure.attach(str(response.status_code), name='Code HTTP')
    allure.attach(response.text, name= "Response API")

    responseBody = response.json()
    print_json(data=responseBody)

    assert responseBody["id"] == 1763233507
    assert responseBody["name"] == "UssopSama"
    assert response.status_code == 200

    print(response.status_code)
    print(response.text)