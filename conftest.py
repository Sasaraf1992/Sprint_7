import allure
import pytest
from endpoints.create_courier_object import CreateCourier
from data import ScooterTestData as SD


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
