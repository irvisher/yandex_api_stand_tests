import data
import sender_stand_request


def change_kit_body(query):
    new_kit_body = data.kit_body.copy()
    new_kit_body["name"] = query
    return new_kit_body


def positive_assert(kit_body):
    kit_body = change_kit_body(kit_body)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token=sender_stand_request.auth_token)

    assert kit_response.status_code == 201
    assert kit_body["name"] == kit_response.json()["name"]


def negative_assert(kit_body):
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token=sender_stand_request.auth_token)
    #assert len(kit_body['name']) >= 1 # если оставить эту проверку, в тесте на недопустимое количество символов будет указана конкретная причина, почему тест не прошёл (длина строки меньше 1 (заданный параметр != 1))
    #assert len(kit_body['name']) <= 511 # если оставить эту проверку, в тесте на недопустимое количество символов будет указана конкретная причина, почему тест не прошёл (длина строки больше 511 (заданный параметр != 511))
    assert kit_response.status_code == 400


# Тест 1. Допустимое количество символов в строке(1)
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")


# Тест 2. Допустимое количество символов в строке(511)
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(
        'AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC')


# Тест 3. Ошибка. Количество символов в строке меньше допустимого (0)
def test_create_kit_zero_letter_in_name_get_unsuccess_response():
    kit_body = change_kit_body("")
    negative_assert(kit_body)


# Тест 4. Ошибка. Количество символов в строке больше допустимого (512)
def test_create_kit_largest_letter_in_name_get_unsuccess_response():
    kit_body = change_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)


# Тест 5. Параметр состоит из строки с английскими буквами
def test_create_kit_english_letters_allowed_get_success_response():
    positive_assert("QWErty")


# Тест 6. Параметр состоит из строки с русскими буквами
def test_create_kit_russian_letters_allowed_get_success_response():
    positive_assert("Мария")


# Тест 7. Параметр состоит из строки специальных символов
def test_create_kit_special_symbols_allowed_get_success_response():
    positive_assert('""№%@","')


# Тест 8. Параметр состоит из строки с пробелами
def test_create_kit_spaces_allowed_get_success_response():
    positive_assert(" Человек и КО ")


# Тест 9. Параметр состоит из строки цифр
def test_create_kit_numbers_allowed_get_success_response():
    positive_assert("123")


# Тест 10. Ошибка. Параметр не передан в запросе
def test_create_kit_parameter_not_passed_get_unsuccess_response():
    kit_body = change_kit_body({})
    negative_assert(kit_body)


# Тест 11. Ошибка. Передан другой тип параметра (число)
def test_create_kit_different_parameter_type_get_unsuccess_response():
    kit_body = change_kit_body(123)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token=sender_stand_request.auth_token)

    #assert isinstance(kit_response.json()['name'], str) #если использовать эту проверку тест также упадёт, но будет указана конкретная причина почему - несоответствие типа данных в заданном параметре
    assert kit_response.status_code == 400