import pytest
import requests
import allure
import json
from data import *
from generators import *
from helps import *

class TestCreateOrder:
    @allure.title('Тест на оформление заказа с разным выбором цветов самоката')
    @allure.description('Отправляем POST-Запросы для заказа самоката, поочереди выбирая разные цвета самоката')
    @pytest.mark.parametrize('color', [{"color": ["BLACK"]}, {"color": ["GREY"]}, {"color": ["BLACK", "GRAY"]}, {"color": [""]}])
    def test_create_order(self, color):
        headers = {'Content-Type': 'application/json'}
        # Используем данные для оформления заказа
        data = DataForOrder.order_data
        data = json.dumps(data)
        # Используем POST-Запрос для оформления заказа
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATE_AN_ORDER}', headers=headers, data=data)
        # Получаем код 201 и 'track'
        assert response.status_code == 201
        assert 'track' in response.text
