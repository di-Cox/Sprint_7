from generators import *



    # Главная страница и ручки-запросов
class Url:
    MAIN_URL = 'https://qa-scooter.praktikum-services.ru/'      # Главная страница "Яндекс Самокат"
    COURIER_LOGIN = 'api/v1/courier/login'      # POST-Запрос на Логин курьера в системе
    CREATING_COURIER = 'api/v1/courier'         # POST-Запрос на Создание курьера
    DELETE_COURIER = 'api/v1/courier/:id'       # DELETE-Запрос на Удаление курьера
    RECEIVE_ORDER_COURIER = 'api/v1/courier/:id/ordersCount'    # GET-Запрос для Получения количество заказов курьера
    COMPLETE_ORDER = 'api/v1/orders/finish/:id'         # PUT-Запрос для Завершения заказа
    CANCEL_ORDER = 'api/v1/orders/cancel'           # PUT-Запрос для Отмены заказа
    GETTING_LIST_ORDERS = 'api/v1/orders'           # GET-Запрос для Получения списка заказов
    RECEIVE_ORDER_ITS_NUMBER = 'api/v1/orders/track'    # GET-Запрос для Получения заказа по его номеру
    ACCEPT_ORDER = 'api/v1/orders/accept/:id'       # PUT-Запрос для Принятия заказа
    CREATE_AN_ORDER = 'api/v1/orders'           # POST-Запрос для Создания заказа
    PING_SERVER = 'api/v1/ping'         # GET-Запрос для Пинга сервера
    SEARCH_METRO = 'api/v1/stations/search'     # GET-Запрос для Поиска станций метро по названию



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


