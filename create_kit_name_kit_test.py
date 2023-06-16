import data
import sender_stand_request
import requests
import configuration
'''
def test_create_user():
    response0 = sender_stand_request.post_new_user()

    assert response0.status_code == 201
    token = response0.json()["authToken"]
    assert token != ""
    '''

def get_kit_body(name):

    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body


def check_name():
    kits_table_response = sender_stand_request.get_kits_table()

    str_kits = kit_body["name"] + "," + kit_body["card"] + "," \
               + kit_body["id"] + kit_body['name'] \
            + kit_body["productsList"] + kit_body["id"] + kit_body["productsCount"] + ",,," + kit_response.json()["authToken"]

    assert check_name().text.count(str_kits) == 1



# Функция для негативной проверки
def negative_assert(name):
    kit_body = get_kit_body(name)
    kit_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=kit_body, headers=data.kit_header)

    # kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)


    assert kit_response.status_code == 400

    # Проверка, что в теле ответа атрибут "code" равен 400
    assert kit_response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert kit_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "длина должна быть не менее 2 и не более 15 символов"
#1
def test_create_kit_1_letter_in_name_get_success_response():
    kit_body = get_kit_body("а")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)

    assert kit_response.status_code == 201
    #assert kit_response == data.kit_body["name"] #В ответе поле name совпадает с полем name в запросе - доделай
#2
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)

    assert kit_response.status_code == 201
    # assert kit_response == data.kit_body["name"] #В ответе поле name совпадает с полем name в запросе - доделай
#3
def test_create_kit_zero_letter_in_name_get_unsuccess_response():
    negative_assert('')


#4
#5
#6
#7
#8
#9
#10
#11