import pytest
import requests
import allure
from data import *
from generators import *
from helps import *

class TestLoginCourier:
    @allure.title('Тест на авторизацию курьера с корректными данными')
    @allure.description('Отправляем POST-Запрос на авторизацию, получаем ответ и удаляем курьера')
    def test_login_courier(self, courier_reg_log_del):
        # Используем фикстуру
        courier_data = courier_reg_log_del
        # Используем авторизацию курьера с помощью класса 'CourierRegistration' и метода 'login_courier'
        response = CourierRegistration().login_courier(courier_data['data'])
        # Получаем код 200 и 'id' курьера
        assert response['response_status_code'] == 200
        assert response.get('id')


    @allure.title('Тест на воспроизведения ошибки при авторизации курьера без заполнения обязательных полей')
    @allure.description('Отправляем POST-Запросы на авторизацию без заполнения обязательных полей')
    @pytest.mark.parametrize('courier_data', [DataForRegistration.data_courier_login_without_login,
                                              DataForRegistration.data_courier_login_without_password])
    def test_login_courier_without_login_and_password(self, courier_data):
        # Используем POST-Запрос на авторизацию курьера без заполнения обязательных полей
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', data=courier_data)
        # Получаем код 400 и ответ об ошибке
        assert response.status_code == 400
        assert 'Недостаточно данных для входа' in response.text


    @allure.title('Тест на воспроизведения ошибки при авторизации курьера c некорректными данными')
    @allure.description('Отправляем POST-Запросы на авторизацию с некорректными данными')
    def test_login_courier_incorrect(self):
        # Используем POST-Запрос на авторизацию курьера с некорректными данными
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', data=DataForRegistration.data_courier_login_incorrect)
        # Получаем код 404 и ответ об ошибке
        assert response.status_code == 404
        assert 'Учетная запись не найдена' in response.text
