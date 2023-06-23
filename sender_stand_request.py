import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER, json=body, headers=data.headers)

response = post_new_user(data.user_body)

auth_token = response.json()['authToken']
print(response, auth_token)


def get_token(auth_token):
    return "Bearer " + auth_token

def post_new_client_kit(kit_body, auth_token):
    headers_dict = data.headers.copy()
    headers_dict["Authorization"] = get_token(auth_token)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT, json=kit_body, headers=headers_dict)

response = post_new_client_kit(data.kit_body, auth_token)

print(response, response.json())



