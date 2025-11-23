import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *

config = config()
base = config['API']['base_url']
orderID = 9223372036854761016
url = f"{base}{store.orderById.format(orderID=orderID)}"


def test_delete_an_order_by_ID():
    with allure.step('delete an order by ID'):
        response = requests.delete(url)

        allure.attach(response.text, name='API response')
        allure.attach(str(response.status_code), name='Code HTTP')

        body = response.json()
        print_json(data=body)

        assert response.status_code == 200