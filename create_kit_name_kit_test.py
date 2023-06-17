import data
import sender_stand_request


def test_get_new_user():
    res = sender_stand_request.post_new_user(data.user_body)

    assert res.status_code == 201
    token = res.json()["authToken"]
    assert token != ""


'''def cng_kit_body(name):
    new_kit_body = data.kit_body.copy()
    new_kit_body["name"] = name
    return new_kit_body'''


def change_kit_body(kit_body):
    new_kit_body = data.kit_body.copy()
    new_kit_body["name"] = kit_body
    return new_kit_body

def positive_assert(name):
    kit_body = change_kit_body(name)
    print(kit_body)

    kit_response = sender_stand_request.post_new_client_kit(data.kit_body, data.auth_token, data.kit_header)
    print(kit_response, kit_response.status_code)
    assert kit_response.status_code == 201

    '''kit_table_response = sender_stand_request.get_kits_table()

    str_kits = (
            kit_body["name"] + ","
            + kit_body["card"] + "," + kit_body["id"]
            + kit_body['name'] + ","
            + kit_body["productsList"] + ","
            + kit_body["id"] + kit_body["productsCount"]
    )
    assert kit_table_response.text.count(str_kits) == 1'''

#kit_body -> str : name для изменения объекта kit_body
def negative_assert(kit_body):

    if kit_body is None:
        kit_body = {
        # 'name': ''
        }
    #do not work now ?(
    elif not kit_body:
        kit_body = {
            "name": None
            # 'name': ''
        }
    else:
        kit_body = change_kit_body(kit_body)

    res = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)

    assert res.status_code == 400
    assert res.json()["code"] == 400
    assert res.json()["message"] == "Имя пользователя введено некорректно. " \
                                    "Имя может содержать только русские или латинские буквы, " \
                                    "длина должна быть не менее 1 и не более 511 символов"


# 'Unexpected token ' in JSON at position 0' !=  - исправить

# 1
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("а")
    # В ответе поле name совпадает с полем name в запросе - доделай


# 2
def test_create_kit_511_letter_in_name_get_success_response():
    kit_body = change_kit_body(
        "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    kit_response = sender_stand_request.post_new_client_kit(kit_body, data.auth_token, data.kit_header)

    assert kit_response.status_code == 201
    # В ответе поле name совпадает с полем name в запросе - доделай


# 3
def test_create_kit_zero_letter_in_name_get_unsuccess_response():
    negative_assert('')


# 'Unexpected token ' in JSON at position 0' !=  - исправить
# 4
def test_create_kit_largest_letter_in_name_get_unsuccess_response():
    negative_assert(
        'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD')
    # 'Unexpected token ' in JSON at position 0' !=  - исправить


# 5
def test_create_kit_english_letters_allowed_get_success_response():
    positive_assert("QWErty")


# 6
def test_create_kit_russian_letters_allowed_get_success_response():
    positive_assert("Мария")


# 7
def test_create_kit_special_symbols_allowed_get_success_response():
    positive_assert('""№%@","')


# 8
def test_create_kit_spaces_allowed_get_success_response():
    positive_assert(" Человек и КО ")


# 9
def test_create_kit_numbers_allowed_get_success_response():
    positive_assert("123")


# 10
def test_create_kit_parameter_not_passed_get_unsuccess_response():
    negative_assert(None)


# 11
def test_create_kit_different_parameter_type_get_unsuccess_response():
    negative_assert(123)
