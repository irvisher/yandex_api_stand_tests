import configuration
import requests
import data
'''
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

print(get_docs().status_code)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count": 20})

print(get_logs().status_code)
print(get_logs().headers)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

print(get_users_table().status_code)
'''
def get_kits_table():
    return requests.get(configuration.URL_SERVICE + configuration.KITS_TABLE_PATH)

print(get_kits_table().status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.headers)

response = post_new_user(data.user_body)
token = response.json()['authToken']
print(response, token)


def post_new_client_kit(kit_body, auth_token, kit_header):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=kit_body, headers=kit_header)

response = post_new_client_kit(data.kit_body, data.auth_token, data.kit_header) #Authorization
print(response.json())


'''
def change_kit_body():
    new_kit_body = data.kit_body.copy()
    new_kit_body["name"] = "a"
    return new_kit_body
print(change_kit_body)'''

