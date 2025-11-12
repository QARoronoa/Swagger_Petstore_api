import os
import allure
import requests
from utilities.configuration import config
from utilities.ressources import apiRessources

cfg = config()
base = cfg['API']["base_url"]

pet_id = 1762962870
url = f"{base}{apiRessources.postImage.format(petId=pet_id)}"
path_image = r"C:\Users\Administrateur\Pictures\nav.PNG"

#verification image
assert os.path.exists(path_image)

#test
def test_upload_une_image():
    with allure.step('appel POST/uploadImage'):
        with open(path_image, 'rb') as f:
            response = requests.post(url, files={'file':f}, timeout=10)

#allure attach
    allure.attach(str(response.status_code))
    allure.attach(response.text)

#assert
    assert response.status_code == 200
