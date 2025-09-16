import pytest
import requests
import allure
from data import *
from helps import CourierRegistration
from generators import *


class TestCreateCourier:
    @allure.title('Тест на создание нового курьера')
    @allure.description('Отправляем POST-Запрос на создание нового курьера, получаем ответ и удаляем курьера')
    def test_create_courier_registration(self, courier_reg_log_del):
        # Данные и ответ, возвращённые фикстурой (фикстура зарегистрировала курьера)
        with allure.step('Получить данные созданного курьера из фикстуры'):
            created = courier_reg_log_del
            courier_data = created['data']

        # Проверяем, что фикстура зарегистрировала курьера корректно
        with allure.step('Проверить статус код ответа при создании'):
            assert created['response_status_code'] == 201

        with allure.step('Проверить тело ответа при создании'):
            assert created['response_text'] == '{"ok":true}'

        # Дополнительно проверим, что можно залогиниться под этими данными
        with allure.step('Проверить логин созданного курьера'):
            login_response = CourierRegistration().login_courier(courier_data)
            assert login_response['response_status_code'] == 200
            assert login_response.get('id')

    @allure.title('Тест на воспроизведения ошибки при создании двух одинаковых аккаунтов курьера')
    @allure.description('Отправляем два POST-Запроса на регистрацию курьера')
    def test_create_courier_registration_duplicate(self, courier_reg_log_del):
        # Используем данные курьера, созданного фикстурой
        with allure.step('Получить данные первого курьера из фикстуры'):
            data_courier = courier_reg_log_del['data']

        # Повторный запрос на создание (должен вернуть конфликт)
        with allure.step('Отправить повторный запрос на создание курьера с теми же данными'):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', data=data_courier)

        with allure.step('Проверить статус код конфликта'):
            assert response.status_code == 409

        with allure.step('Проверить сообщение об ошибке'):
            assert 'Этот логин уже используется' in response.text

    @allure.title('Тест на воспроизведения ошибки при создании курьера без заполнения обязательных полей')
    @allure.description('Отправляем POST-Запросы на регистрацию без заполнения обязательных полей')
    @pytest.mark.parametrize('courier_data', [DataForRegistration.data_courier_login_without_login,
                                              DataForRegistration.data_courier_login_without_password])
    def test_create_courier_login_without_login_and_password(self, courier_data):
        # Отправляем POST-Запросы с незаполненными полями 'login' и 'password'
        with allure.step('Отправить запрос на создание курьера без обязательного поля'):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', data=courier_data)

        # Получаем код 400 и ответ об ошибке
        with allure.step('Проверить статус код ошибки'):
            assert response.status_code == 400

        with allure.step('Проверить сообщение об ошибке'):
            assert 'Недостаточно данных для создания учетной записи' in response.text
