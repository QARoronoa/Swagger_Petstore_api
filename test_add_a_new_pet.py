import time
from rich import print_json
import allure
import requests
from utilities.ressources import *
from utilities.configuration import config

cfg = config()
base = cfg['API']['base_url']
url = f"{base}{apiRessources.addPet}"
pet_id = int(time.time())

payload = {
    "id": pet_id,
    "category": {"id": pet_id, "name": "UssopSama"},
    "name": "UssopSama",
    "photoUrls": ["string"],
    "tags": [{"id": pet_id, "name": "string"}],
    "status": "available"
}

def test_add_new_pet():
    with allure.step('Appel POST /add a pet'):
        response = requests.post(url, json=payload)

        #allure attach
        allure.attach(response.text,name="Réponse API")
        allure.attach(str(response.status_code), name="Code HTTP")

        response_body = response.json()
        print_json(data=response_body)

        assert response.status_code == 200
        assert response_body["id"] == pet_id
        assert response_body["name"] == "UssopSama"
        assert response_body["status"] == "available"