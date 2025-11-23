import allure
import requests
from rich import print_json
from utilities.configuration import *
from utilities.ressources import *

config = config()
base = config['API']['base_url']
url = f"{base}{store.petOrder}"

data={
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2025-11-23T17:51:37.746Z",
  "status": "placed",
  "complete": True
}


def test_place_an_order_for_a_pet():
    with allure.step('place an order for a pet'):
        response = requests.post(url, json=data)

    allure.attach(response.text, name= 'API response')
    allure.attach(str(response.status_code), name='Code HTTP')

    body = response.json()
    print_json(data=body)
    print(response.status_code)
