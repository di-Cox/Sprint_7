import pytest
import requests
import allure
from data import *
from helps import CourierRegistration
from generators import *
from curl import *



class TestDeleteCourier:
    @allure.title('Тест на удаление курьера')
    @allure.description('Отправляем DELETE-Запрос на удаление курьера')
    def test_delete_courier(self, courier_del):
        with allure.step('Получить данные курьера из фикстуры'):
            courier_id = courier_del

        with allure.step('Отправить DELETE-запрос на удаление курьера'):
            response = CourierRegistration().delete_courier(courier_id['id'])

        with allure.step('Проверить статус код успешного удаления'):
            assert response['response_status_code'] == 200

        with allure.step('Проверить тело ответа при удалении'):
            assert response['response_text'] == ErrorMessages.OK_TRUE

    @allure.title('Тест на удаление курьера с некорректным id')
    @allure.description('Отправляем DELETE-Запрос на удаление курьера с несуществующим id')
    def test_delete_courier_incorrect_id(self):
        with allure.step('Создать некорректный id курьера'):
            courier_id = '7777123'

        with allure.step('Отправить DELETE-запрос с некорректным id'):
            response = CourierRegistration().delete_courier(courier_id)

        with allure.step('Проверить статус код ошибки 404'):
            assert response['response_status_code'] == 404

        with allure.step('Проверить сообщение об ошибке'):
            assert ErrorMessages.COURIER_NOT_FOUND in response["response_text"]

    @allure.title('Тест на удаления курьера без id')
    @allure.description('Отправляем DELETE-Запрос на удаление курьера без id')
    def test_delete_courier_none_id_failed(self):
        with allure.step('Использовать None в качестве id'):
            courier_id = None

        with allure.step('Отправить DELETE-запрос без id'):
            response = CourierRegistration().delete_courier(courier_id)

        with allure.step('Проверить статус код ошибки 500'):
            assert response["response_status_code"] == 500

        with allure.step('Проверить сообщение об ошибке синтаксиса'):
            assert ErrorMessages.INVALID_INPUT_SYNTAX in response["response_text"]

