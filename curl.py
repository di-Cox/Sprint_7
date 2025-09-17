
# Класс для хранения Url-Главной страницы и Ручек запросов

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