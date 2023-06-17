import configuration
import requests
import data

""""
def post_create_user():
    req = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER, json=data.user_body)
    return req

print(post_create_user())


def post_create_client_kit():
    req = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT, json=data.kit_body, headers=data.kit_header)
    return req
print(post_create_client_kit())
"""

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER, json=body, headers=data.headers)

response = post_new_user(data.user_body)
token = response.json()['authToken']
print(response, token)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE)

response = get_users_table()
print(response.status_code)

def post_new_client_kit(kit_body, auth_token, kit_header):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT, json=kit_body, headers=kit_header)

response = post_new_client_kit(data.kit_body, data.auth_token, data.kit_header) #Authorization
print(response, response.json())


def get_kits_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE)

res = get_kits_table().status_code
print(res)