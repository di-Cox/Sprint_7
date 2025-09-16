from generators import *
import requests
from data import *


class CourierRegistration:
    # Регистрация курьера
    @staticmethod
    def register_courier():
        # Передаём данные в тело
        data = CourierGenerator.generate_data_couriers()
        # Создаём POST-Запрос на регистрацию
        response = requests.post(f'{Url.MAIN_URL}{Url.CREATING_COURIER}', data=data)
        # Получаем ответ
        return {'response_text': response.text, 'response_status_code': response.status_code, 'data': data}


    @staticmethod
    # Логинимся курьером и получаем id
    def login_courier(data):
        # Создаём POST-Запрос на логин
        response = requests.post(f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', data=data)
        # Получаем ответ и id курьера
        return {'id': str(response.json()['id']), 'response_text': response.text, 'response_status_code': response.status_code}


    @staticmethod
    # Удаление курьера
    def delete_courier(id):
        # Убираем ':id' и подставляем ID через форматирование
        url = Url.DELETE_COURIER.replace(":id", str(id))
        # Создаём DELETE-Запрос на удаление
        response = requests.delete(f'{Url.MAIN_URL}{url}')
        # Получаем ответ
        return {'response_text': response.text, 'response_status_code': response.status_code}
