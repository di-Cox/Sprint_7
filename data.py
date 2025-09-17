from generators import *


    # Данные для оформления заказа самоката
class DataForOrder:
    order_data = {
        'firstName': 'Дмитрий',
        'lastName': 'Волгушев',
        'address': 'Мира 777',
        'metroStation': 3,
        'phone': '89012334455',
        'rentTime': 3,
        'deliveryDate': '2025-09-17',
        'comment': 'Скорее бы словить столб'
    }




    # Класс данных для регистрации курьера
class DataForRegistration:
    # Корректные данные для регистрации курьера
    data_login_courier = CourierGenerator.generate_data_couriers()

    # Некорректные данные для регистрации курьера с пропущенным полем 'login'
    data_courier_login_without_login = CourierGenerator.generate_data_courier_without_login()

    # Некорректные данные для регистрации курьера с пропущенным полем 'password'
    data_courier_login_without_password = CourierGenerator.generate_data_courier_without_password()

    # Несуществующие данные для регистрации курьера
    data_courier_login_incorrect = {
        "login": "Shikamaru777",
        "password": "Naru666"
    }


class ErrorMessages:
    # Класс для хранения всех текстов ошибок API

    # Ошибки создания и работы с курьерами
    LOGIN_ALREADY_EXISTS = "Этот логин уже используется"
    NOT_ENOUGH_DATA_FOR_CREATE = "Недостаточно данных для создания учетной записи"
    COURIER_NOT_FOUND = "Курьера с таким id нет"
    COURIER_ID_REQUIRED = "Недостаточно данных для входа"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    INVALID_INPUT_SYNTAX = "invalid input syntax"
    # Успешные сообщения
    OK_TRUE = '{"ok":true}'
    TRACK_FIELD = "track"
