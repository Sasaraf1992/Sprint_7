import allure
import pytest
from endpoints.create_courier_object import CreateCourier
from data import ScooterTestData as SD
from faker import Faker

fake = Faker()


@allure.step("Создание фейкового курьера")
@pytest.fixture(scope='module')
def fake_courier():
    co = CreateCourier()
    co.courier_creation(data=SD.FAKE_COURIER_CREATION)
    return co


@allure.step("Создание фейкового курьера")
@pytest.fixture(scope='module')
def fake_courier_required_fields():
    co = CreateCourier()
    co.courier_creation(data=SD.FAKE_COURIER_CREATION_ONLY_REQUIRED_FIELDS)
    return co


@pytest.fixture(scope='module')
def fake_courier_required_login_password():
    co = CreateCourier()
    login = fake.user_name()
    password = fake.password()
    co.courier_creation(data={'login': login, 'password': password})
    return login, password
