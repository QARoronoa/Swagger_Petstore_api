import allure
import requests
from rich import print_json
from utilities.ressources import *
from utilities.configuration import *


config = config()
base = config['API']['base_url']
orderID = 9223372036854761016
url = f"{base}{store.orderById.format(orderID=orderID)}"



def test_find_an_order_by_id():
    with allure.step('find an order by id'):
        response = requests.get(url)

        allure.attach(response.text, name='API response')
        allure.attach(str(response.status_code), name='Code HTTP')

        body = response.json()
        print_json(data=body)
        print(response.status_code)

        assert body["id"] == orderID

