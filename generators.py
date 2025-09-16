from faker import Faker


fake = Faker('ru_RU')

class CourierGenerator:
    # Генерация рандомных валидных данных для регистрации
    @staticmethod
    def generate_data_couriers():

        # Генерируем рандомные поля для заполнения
        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()

        data = {
            'login': login,
            'password': password,
            'first_name': first_name
        }

        return data


    # Генерация рандомных данных для регистрации без обязательного поля 'login'
    @staticmethod
    def generate_data_courier_without_login():
        # Генерируем рандомные поля без поля 'login'
        password = fake.password()
        first_name = fake.first_name()

        data = {
            'login':'',
            'password': password,
            'first_name': first_name
        }

        return data



    # Генерация рандомных данных для регистрации без обязательного поля 'password'
    @staticmethod
    def generate_data_courier_without_password():
        # Генерируем рандомные поля без поля 'password'
        login = fake.user_name()
        first_name = fake.first_name()

        data = {
            'login': login,
            'password': '',
            'first_name': first_name
        }

        return data
