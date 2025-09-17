import pytest
import requests
import allure
from data import *
from generators import *
from helps import *
from curl import *


class TestLoginCourier:
    @allure.title('Тест на авторизацию курьера с корректными данными')
    @allure.description('Отправляем POST-Запрос на авторизацию, получаем ответ и удаляем курьера')
    def test_login_courier(self, courier_reg_log_del):
        with allure.step('Получить данные курьера из фикстуры'):
            courier_data = courier_reg_log_del

        with allure.step('Отправить запрос на авторизацию курьера'):
            response = CourierRegistration().login_courier(courier_data['data'])

        with allure.step('Проверить статус код успешной авторизации'):
            assert response['response_status_code'] == 200

        with allure.step('Проверить наличие id в ответе'):
            assert response.get('id')

    @allure.title('Тест на воспроизведения ошибки при авторизации курьера без заполнения обязательных полей')
    @allure.description('Отправляем POST-Запросы на авторизацию без заполнения обязательных полей')
    @pytest.mark.parametrize('courier_data', [DataForRegistration.data_courier_login_without_login,
                                              DataForRegistration.data_courier_login_without_password])
    def test_login_courier_without_login_and_password(self, courier_data):
        with allure.step('Отправить запрос на авторизацию без обязательных полей'):
            response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', data=courier_data)

        with allure.step('Проверить статус код ошибки 400'):
            assert response.status_code == 400

        with allure.step('Проверить сообщение об ошибке'):
            assert ErrorMessages.COURIER_ID_REQUIRED in response.text

    @allure.title('Тест на воспроизведения ошибки при авторизации курьера c некорректными данными')
    @allure.description('Отправляем POST-Запросы на авторизацию с некорректными данными')
    def test_login_courier_incorrect(self):
        with allure.step('Подготовить некорректные данные для авторизации'):
            incorrect_data = DataForRegistration.data_courier_login_incorrect

        with allure.step('Отправить запрос на авторизацию с некорректными данными'):
            response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', data=incorrect_data)

        with allure.step('Проверить статус код ошибки 404'):
            assert response.status_code == 404

        with allure.step('Проверить сообщение об ошибке'):
            assert ErrorMessages.ACCOUNT_NOT_FOUND in response.text
