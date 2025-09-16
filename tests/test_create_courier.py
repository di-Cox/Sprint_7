import pytest
import requests
import allure
from data import *
from helps import CourierRegistration
from generators import *

class TestCreateCourier:
    @allure.title('Тест на создание нового курьера')
    @allure.description('Отправляем POST-Запрос на создание нового курьера, получаем ответ и удаляем курьера')
    def test_create_courier_registration(self):
        # Используем корректные данные для регистрации курьера
        data_courier = DataForRegistration.data_login_courier
        # Отправляем POST-Запрос на создание курьера
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', data=data_courier)
        # Получаем ответ 201 и ответ {"ok":true} и проверяем его
        assert response.status_code == 201
        assert response.text == '{"ok":true}'
        # Отправляем POST-Запрос для логирования
        login_response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', data=data_courier)
        # Получаем 'id' курьера
        courier_id = login_response.json().get('id')
        # Отправляем DELETE-Запрос для удаления курьера, передав 'id'
        requests.delete(f'{Url.MAIN_URL}{Url.DELETE_COURIER}/{courier_id}')


    @allure.title('Тест на воспроизведения ошибки при создании двух одинаковых аккаунтов курьера')
    @allure.description('Отправляем два POST-Запроса на регистрацию курьера')
    def test_create_courier_registration_duplicate(self):
        # Используем корректные данные для регистрации курьера
        data_courier = DataForRegistration.data_login_courier
        # Отправляем первый POST-Запрос на создание курьера
        requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', data=data_courier)
        # Отправляем второй POST-Запрос на создание курьера
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', data=data_courier)
        # Получаем код 409 и ответ об ошибке
        assert response.status_code == 409
        assert 'Этот логин уже используется' in response.text
        # Отправляем POST-Запрос для логирования
        login_response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', data=data_courier)
        # Получаем 'id' курьера
        courier_id = login_response.json().get('id')
        # Отправляем DELETE-Запрос для удаления курьера, передав 'id'
        requests.delete(f'{Url.MAIN_URL}{Url.DELETE_COURIER}/{courier_id}')



    @allure.title('Тест на воспроизведения ошибки при создании курьера без заполнения обязательных полей')
    @allure.description('Отправляем POST-Запросы на регистрацию без заполнения обязательных полей')
    @pytest.mark.parametrize('courier_data', [DataForRegistration.data_courier_login_without_login,
                                              DataForRegistration.data_courier_login_without_password])
    def test_create_courier_login_without_login_and_password(self, courier_data):
        # Отправляем POST-Запросы с незаполненными полями 'login' и 'password'
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', data=courier_data)
        # Получаем код 400 и ответ об ошибке
        assert response.status_code == 400
        assert 'Недостаточно данных для создания учетной записи' in response.text
