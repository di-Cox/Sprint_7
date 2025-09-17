import requests
import allure
from data import *
from generators import *
from helps import *
from curl import *


class TestsGetOrdersList:

    @allure.title('Тест на проверку получения списка заказов')
    @allure.description('Отправляем GET-Запрос и получаем список заказов')
    def test_get_orders_list(self):
        with allure.step('Отправить GET-запрос для получения списка заказов'):
            response = requests.get(f'{Url.MAIN_URL}{Url.GETTING_LIST_ORDERS}')

        with allure.step('Проверить статус код ответа'):
            assert response.status_code == 200

        with allure.step('Проверить наличие track в ответе'):
            assert ErrorMessages.TRACK_FIELD in response.text
