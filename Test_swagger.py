import requests
import pytest

# -------- 1. Сущность Pet ---------
# 1.1 POST upload_an_image
def pet_upload_an_image():
    headers = {
        'accept': 'application/json',
    }
    files = {
    'file': ('suitcase.jpg', open('suitcase.jpg', 'rb'), 'image/jpeg'),
    }
    response = requests.post("https://petstore.swagger.io/v2/pet/0/uploadImage", headers=headers, files=files)
    return response.status_code

def test_pet_upload_an_image():
    assert pet_upload_an_image() == 200

# 1.2 POST Add_a_new_pet_to_the_store
def Add_a_new_pet_to_the_store():
    headers = {
    'accept': 'application/json',
    'Content-Type': 'application/json',
    }

    json_data = {
        'id': 0,
        'category': {
            'id': 0,
            'name': 'string',
        },
        'name': 'doggie',
        'photoUrls': [
            'string',
        ],
        'tags': [
            {
                'id': 0,
                'name': 'Bobby',
            },
        ],
        'status': 'available',
    }
    response = requests.post('https://petstore.swagger.io/v2/pet', headers=headers, json=json_data)
    return response.status_code

def test_Add_a_new_pet_to_the_store():
    assert Add_a_new_pet_to_the_store() == 200

# 1.3 PUT
def update_pet():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'id': 0,
        'category': {
            'id': 0,
            'name': 'string',
        },
        'name': 'doggie',
        'photoUrls': [
            'string',
        ],
        'tags': [
            {
                'id': 0,
                'name': 'string',
            },
        ],
        'status': 'available',
    }
    response = requests.put('https://petstore.swagger.io/v2/pet', headers=headers, json=json_data)
    return response.status_code

def test_update_pet():
    assert update_pet() == 200

# 1.4 GET
def Finds_pet_by_status():
    headers = {
        'accept': 'application/json',
    }
    params = {
        'status': 'available',
    }

    response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus', params=params, headers=headers)
    return response.status_code

def test_Finds_pet_by_status():
    assert Finds_pet_by_status() == 200

# 1.5 DELETE
def Deletes_pet():
    headers = {
        'accept': 'application/json',
    }

    response = requests.delete('https://petstore.swagger.io/v2/pet/1', headers=headers)
    return response.status_code

def test_Deletes_pet():
    assert Deletes_pet() == 200
    assert Deletes_pet() == 404

# -------- 2. Сущность Store ---------
# 2.1 POST
def Place_an_order():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'id': 1,
        'petId': 1,
        'quantity': 1,
        'shipDate': '2024-02-03T10:16:43.279Z',
        'status': 'placed',
        'complete': False,
    }

    response = requests.post('https://petstore.swagger.io/v2/store/order', headers=headers, json=json_data)
    return response.status_code

def test_Place_an_order():
    assert Place_an_order() == 200

# 2.2 POST №2 invalid input
def Place_an_order_invalid_order():    
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }
    json_data = {
        'id': "a",
        'petId': 1,
        'quantity': 0,
        'shipDate': '2024-02-03T10:16:43.279Z',
        'status': '1',
        'complete': True,
    }
    response = requests.post('https://petstore.swagger.io/v2/store/order', headers=headers, json=json_data)
    return response.status_code

def test_Place_an_order_invalid_order():
    assert Place_an_order_invalid_order() == 500

# 2.3 GET
def Find_purchase():
    headers = {
        'accept': 'application/json',
    }

    response = requests.get('https://petstore.swagger.io/v2/store/order/1', headers=headers)
    return response.status_code

def test_Find_purchase():
    assert Find_purchase() == 200

# 2.4 DELETE
def Delete_purchase_order():
    headers = {
        'accept': 'application/json',
    }

    response = requests.delete('https://petstore.swagger.io/v2/store/order/1', headers=headers)
    return response.status_code
def test_Delete_purchase_order():
    assert Delete_purchase_order() == 200
    assert Delete_purchase_order() == 404

# 2.5 DELETE №2
def Delete_purchase_order_notfound():
    headers = {
        'accept': 'application/json',
    }
    response = requests.delete('https://petstore.swagger.io/v2/store/order/1222', headers=headers)
    return response.status_code

def test_Delete_purchase_order_notfound():
    assert Delete_purchase_order_notfound() == 404
# -------- 3. Сущность User ---------

# 3.1 POST
def Create_list():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = [
        {
            'id': 0,
            'username': 'string',
            'firstName': 'string',
            'lastName': 'string',
            'email': 'string',
            'password': 'string',
            'phone': 'string',
            'userStatus': 0,
        },
    ]

    response = requests.post('https://petstore.swagger.io/v2/user/createWithArray', headers=headers, json=json_data)
    return response.status_code

def test_Create_list():
    assert Create_list() == 200

# 3.2 GET
def get_user_by_name():
    headers = {
        'accept': 'application/json',
    }

    response = requests.get('https://petstore.swagger.io/v2/user/Joe', headers=headers)
    return response.status_code

def test_get_user_by_name():
    assert get_user_by_name() == 404

# 3.3 PUT
def update_user():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'id': 0,
        'username': 'string',
        'firstName': 'string',
        'lastName': 'string',
        'email': 'string',
        'password': 'string',
        'phone': 'string',
        'userStatus': 0,
    }

    response = requests.put('https://petstore.swagger.io/v2/user/Bob', headers=headers, json=json_data)
    return response.status_code

def test_update_user():
    assert update_user() == 200

# 3.4 DELETE
def delete_user():
    headers = {
        'accept': 'application/json',
    }

    response = requests.delete('https://petstore.swagger.io/v2/user/Bob', headers=headers)
    return response.status_code

def test_delete_user():
    assert delete_user() == 404

# 3.5 POST №2
def create_user():    
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json',
    }

    json_data = {
        'id': 0,
        'username': 'string',
        'firstName': 'string',
        'lastName': 'string',
        'email': 'string',
        'password': 'string',
        'phone': 'string',
        'userStatus': 0,
    }

    response = requests.post('https://petstore.swagger.io/v2/user', headers=headers, json=json_data)
    return response.status_code

def test_create_user():
    assert create_user() == 200

