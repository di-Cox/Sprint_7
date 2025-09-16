import pytest
import requests
import allure
from data import *
from helps import CourierRegistration
from generators import *

class TestDeleteCourier:
    @allure.title('Тест на удаление курьера')
    @allure.description('Отправляем DELETE-Запрос на удаление курьера')
    def test_delete_courier(self, courier_del):
        # Используем фикстуру 'courier_del'
        courier_id = courier_del
        # С помощью класса 'CourierRegistration' и метода 'delete_courier' делаем запрос на удаление
        response = CourierRegistration().delete_courier(courier_id['id'])
        # Получаем код 200 и ответ '{"ok":true}'
        assert response['response_status_code'] == 200
        assert response['response_text'] == '{"ok":true}'


    @allure.title('Тест на удаление курьера с некорректным id')
    @allure.description('Отправляем DELETE-Запрос на удаление курьера с несуществующим id')
    def test_delete_courier_incorrect_id(self):
        # Создаём некорректный id
        courier_id = '7777123'
        # С помощью класса 'CourierRegistration' и метода 'delete_courier' делаем запрос на удаление
        response = CourierRegistration().delete_courier(courier_id)
        # Получаем код 404 и ответ об ошибке
        assert response['response_status_code'] == 404
        assert "Курьера с таким id нет" in response["response_text"]

    @allure.title('Тест на удаления курьера без id')
    @allure.description('Отправляем DELETE-Запрос на удаление курьера без id')
    def test_delete_courier_none_id_failed(self):
        # Id отсутствует
        courier_id = None
        # С помощью класса 'CourierRegistration' и метода 'delete_courier' делаем запрос на удаление
        response = CourierRegistration().delete_courier(courier_id)
        # Получаем код 500 и ответ об ошибке
        assert response["response_status_code"] == 500
        assert "invalid input syntax" in response["response_text"]

