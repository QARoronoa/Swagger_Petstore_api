
class apiRessources :
      postImage = '/pet/{petId}/uploadImage'
      addPet = "/pet"
      updatePet = "/pet"
      statusPet = "/pet/findByStatus"
      findpetId = "/pet/{petId}"
      storeInventory = "/store/inventory"


class store :
      petInventory = '/store/invntory'
      petOrder = '/store/order'
      orderById = "/store/order/{orderID}"

class user :
      creat_list_users = "/user/createWithList"
      get_user_by_name = "/user/{username}"
      user_login = "/user/login"
      user_logout = "/user/logout"
