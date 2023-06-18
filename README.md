﻿# Тесты на проверку параметра 'name' при создании набора пользователя после создания пользователя в Яндекс.Прилавок с помощью API Яндекс.Прилавок.
 
- Разбработка тестов ведется в среде PyCharm на ЯП Python;
- В проекте содержится 6 файлов: 'RAEDME.md', 'gitignore', 'configuration.py', 'data.py', 'sender_stand_request.py', 'create_kit_name_kit_test.py';
- Файл 'configuration.py' содержит ссылку на Яндекс.Прилавок, а т.ж. API каталогов;
- Файл 'data.py' содержит данные для POST-запросов
- Файл 'sender_stand_request.py' содержит функции, которые отправляют POST-запросы(создание пользователя, создание набора)и GET-запросы(к таблицам пользователей и наборов),
- Файл 'create_kit_name_kit_test.py' содержит 13 проверок и три функции, одна тестовая, одна для позитивных проверок, одна для негативных;
- Чек-лист проверок из задания содержит 11 проверок: 4 негативных и 7 позитивных;
- Для запуска тестов в среде разработки должны быть установлены библиотеки 'pytest' и 'requests', а также настроена конфигурация 'Python' - > 'pytest';
- Запуск всех тестов выполянется командой"Debug'pytest'" -> ![image](https://github.com/irvisher/yandex_api_stand_tests/assets/53014420/4821104b-d3a2-4f4e-a555-af5ca9d82edf);
  
#Результаты:
<!DOCTYPE html>
<html>
<head>
<style>
table {
  font-family: arial;
  border-collapse: collapse;
  width: 100%;
}

td, th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>Чек-лист</h2>

<table>
  <tr>
    <th>№</th>
    <th>Описание</th>
    <th>ОР</th>
    <th>Статус выполнения</th>
  </tr>
  <tr>
    <td>1</td>
    <td>Допустимое количество символов (1):
	kit_body = {
	"name": "a"
	}</td>
    <td>Код ответа — 201
	В ответе поле name совпадает с полем name в запросе</td>
	<td>Осталась вторая часть задания</td>
  <tr>
    <td>2</td>
    <td>Допустимое количество символов (511):
	kit_body = {
	"name":"Тестовое значение для этой проверки лучше смотреть в 		коде"
	}</td>
    <td>Код ответа — 201
	В ответе поле name совпадает с полем name в запросе</td>
	<td>Осталась вторая часть задания</td>
  </tr>
    <tr>
    <td>3</td>
    <td>Количество символов меньше допустимого (0):
	kit_body = {
	"name": ""
	}</td>
    <td>Код ответа — 400</td>
	<td>Пока не готово, проблема с токеном</td>
  </tr>
    <tr>
    <td>4</td>
    <td>Количество символов больше допустимого (512):
	kit_body = {
	"name":"Тестовое значение для этой проверки лучше смотреть в 		коде"
	}</td>
    <td>Код ответа — 400</td>
	<td>Пока не готово, проблема с токеном</td>
  </tr>
    <tr>
    <td>5</td>
    <td>Разрешены английские буквы:
	kit_body = {
	"name": "QWErty"
	}</td>
    <td>Код ответа — 201
	В ответе поле name совпадает с полем name в запросе</td>
	<td>Осталась вторая часть задания</td>
  </tr>
    <tr>
    <td>6</td>
    <td>Разрешены русские буквы:
	kit_body = {
	"name": "Мария"
	}</td>
    <td>Код ответа — 201
	В ответе поле name совпадает с полем name в запросе</td>
	<td>Осталась вторая часть задания</td>
  </tr>
    <tr>
    <td>7</td>
    <td>Разрешены спецсимволы:
	kit_body = {
	"name": ""№%@","
	}</td>
    <td>Код ответа — 201
	В ответе поле name совпадает с полем name в запросе</td>
	<td>Осталась вторая часть задания</td>
  </tr>
    <tr>
    <td>8</td>
    <td>Разрешены пробелы:
	kit_body = {
	"name": " Человек и КО "
	}</td>
    <td>Код ответа — 201
	В ответе поле name совпадает с полем name в запросе</td>
	<td>Осталась вторая часть задания</td>
  </tr>
    <tr>
    <td>9</td>
    <td>Разрешены цифры:
	kit_body = {
	"name": "123"
	}</td>
    <td>Код ответа — 201
	В ответе поле name совпадает с полем name в запросе</td>
	<td>Осталась вторая часть задания</td>
  </tr>
    <tr>
    <td>10</td>
    <td>Параметр не передан в запросе:
	kit_body = {
	}</td>
    <td>Код ответа — 400</td>
	<td>Пока не готово, проблема с токеном</td>
  </tr>
    <tr>
    <td>11</td>
    <td>Передан другой тип параметра (число):
	kit_body = {
	"name": 123
	}</td>
    <td>Код ответа — 400</td>
	<td>Пока не готово, проблема с токеном</td>
  </tr>
</table>

</body>
</html>

