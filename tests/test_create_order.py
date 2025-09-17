import pytest
import requests
import allure
import json
from data import *
from generators import *
from helps import *
from curl import *


class TestCreateOrder:
    @allure.title('Тест на оформление заказа с разным выбором цветов самоката')
    @allure.description('Отправляем POST-Запросы для заказа самоката, поочереди выбирая разные цвета самоката')
    @pytest.mark.parametrize('color',
                             [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": ["BLACK", "GRAY"]}, {"color": [""]}])
    def test_create_order(self, color):
        with allure.step('Подготовили заголовки запроса'):
            headers = {'Content-Type': 'application/json'}

        with allure.step('Использовали данные для оформления заказа'):
            data = DataForOrder.order_data

        with allure.step('Выбираем цвет самоката'):
            data.update(color)

        with allure.step('Преобразовать данные в JSON'):
            data = json.dumps(data)

        with allure.step('Отправили POST-запрос для оформления заказа'):
            response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_AN_ORDER}', headers=headers, data=data)

        with allure.step('Проверить статус код ответа'):
            assert response.status_code == 201

        with allure.step('Проверить наличие track в ответе'):
            assert ErrorMessages.TRACK_FIELD in response.text
