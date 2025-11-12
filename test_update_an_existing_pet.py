import allure

from utilities.ressources import *
from utilities.configuration import *
import requests
from rich import print_json

cfg= config()
base = cfg['API']['base_url']
url = f"{base}{apiRessources.updatePet}"
petID = 17629624871

payload = {
  "id": petID,
  "category": {
    "id": petID,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": petID,
      "name": "string"
    }
  ],
  "status": "available"
}


def test_update_existingPet():
    with allure.step("Appel PUT/update pet"):
        response = requests.put(url, json=payload)

        allure.attach(str(response.status_code), name= "Code HTTP")
        allure.attach(response.text, name="Réponse API")

        responseBody = response.json()
        print_json(data=responseBody)

        assert response.status_code == 200
        assert responseBody["id"] == petID


