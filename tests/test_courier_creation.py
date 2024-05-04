import allure

from data import ScooterTestData as SD
from faker import Faker
import pytest
from endpoints.create_courier_object import CreateCourier

fake = Faker()


class TestCourierCreation:

    @allure.title('Проверка, что курьера можно создать')
    def test_courier_successful_creation(self, fake_courier):
        fake_courier.check_status_code_and_text(201, 'ok', True)

    @allure.title('Проверка, что нельзя создать дубликат курьера')
    def test_courier_duplicate_creation_failed(self, fake_courier_required_fields):
        cc = CreateCourier()
        cc.courier_creation(data=SD.FAKE_COURIER_CREATION_ONLY_REQUIRED_FIELDS)
        cc.check_status_code_and_text(409, 'message', 'Этот логин уже используется. Попробуйте другой.')

    @allure.title('Проверка успешного создания курьера при заполнении только рекомендуемых полей')
    def test_courier_required_fields_only(self, fake_courier_required_fields):
        fake_courier_required_fields.check_status_code_and_text(201, 'ok', True)

    @allure.title('Проверка, что если заполненино только одно рекомендуемое поле, возвращается ошибка')
    @pytest.mark.parametrize("login, password", [(fake.user_name(), None), (None, fake.password())])
    def test_courier_required_fields_one_missed_fail(self, login, password):
        cc = CreateCourier()
        cc.courier_creation(data={"login": login, "password": password})
        cc.check_status_code_and_text(400, 'message', "Недостаточно данных для создания учетной записи")
