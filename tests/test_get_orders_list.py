import requests
import allure
from data import *
from generators import *
from helps import *


class TestsGetOrdersList:

    @allure.title('Тест на проверку получения списка заказов')
    @allure.description('Отправляем GET-Запрос и получаем список заказов')
    def test_get_orders_list(self):
        # Отправляем GET-Запрос для получения списка заказов
        response = requests.get(f'{Url.MAIN_URL}{Url.GETTING_LIST_ORDERS}')
        # Получаем код 200 и 'track'
        assert response.status_code == 200
        assert 'track' in response.text
