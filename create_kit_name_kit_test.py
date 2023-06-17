import data
import sender_stand_request
import requests
import configuration
#0
def test_get_new_user():
    res = sender_stand_request.post_new_user(data.user_body)

    assert res.status_code == 201
    token = res.json()["authToken"]
    assert token != ""

'''#01
def test_create_kit_1_letter_in_name_get_success_response():
    body = sender_stand_request.change_kit_body()
    req = sender_stand_request.post_new_client_kit(body, data.auth_token, data.kit_header).status_code
    assert req == 201
    #нужна ещё часть с "в ответе поле name совпадает с полем name в запросе"
    '''
def change_kit_body(name):
    new_kit_body = data.kit_body.copy()
    new_kit_body["name"] = name
    return new_kit_body
#print(change_kit_body(), )

#+
def positive_assert(name):
    kit_body = change_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)


    assert kit_response.status_code == 201


    str_kits = kit_body["name"] + "," + kit_body["card"] + ","  + kit_body["id"] + kit_body['name'] + kit_body["productsList"] + kit_body["id"] + kit_body["productsCount"]

print(positive_assert().json())
#+

#-


'''

def check_name():
    kits_table_response = sender_stand_request.get_kits_table()

    str_kits = kit_body["name"] + "," + kit_body["card"] + "," \
               + kit_body["id"] + kit_body['name'] \
            + kit_body["productsList"] + kit_body["id"] + kit_body["productsCount"] + ",,," + kit_response.json()["authToken"]

    assert check_name().text.count(str_kits) == 1


# Функция для позитивной проверки



# Функция для негативной проверки
def negative_assert(name):
    kit_body = get_kit_body(name)
    # kit_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH, json=kit_body, headers=data.kit_header)

    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)


    assert kit_response.status_code == 400

    # Проверка, что в теле ответа атрибут "code" равен 400
    assert kit_response.json()["code"] == 400
    # Проверка текста в теле ответа в атрибуте "message"
    assert kit_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "длина должна быть не менее 1 и не более 511 символов"
#1
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("а")
    #assert kit_response == data.kit_body["name"] #В ответе поле name совпадает с полем name в запросе - доделай
#2
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)

    assert kit_response.status_code == 201
    # assert kit_response == data.kit_body["name"] #В ответе поле name совпадает с полем name в запросе - доделай
#3
def test_create_kit_zero_letter_in_name_get_unsuccess_response():
    negative_assert('') #нужен ответ от сервера 400, а не как приходит, 201


#4
def test_create_kit_largest_letter_in_name_get_unsuccess_response():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)

    assert kit_response.status_code == 400 #нужен ответ от сервера 400, а не как приходит, 201
#5
#6
#7
#8
#9
#10
#11

'''