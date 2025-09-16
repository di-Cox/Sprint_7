import pytest
import logging
from helps import *
from data import *
from generators import *

logger = logging.getLogger(__name__)

# Создаём фикстуру для регистрации, логирования и удаления курьера
@pytest.fixture()
def courier_reg_log_del():
    courier_create = CourierRegistration().register_courier()
    courier_login = CourierRegistration().login_courier(courier_create['data'])
    yield courier_create
    CourierRegistration().delete_courier(courier_login['id'])


# Создаём фикстуру с регистрацией и закомментированым лоигрованием, если оно понадобится
@pytest.fixture()
def courier_del():
    courier_create = CourierRegistration().register_courier()
    #logger.info(courier_create['data']) # Если понадобился логироаться
    courier_login = CourierRegistration().login_courier(courier_create['data'])
    yield courier_login

