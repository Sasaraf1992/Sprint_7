from data import ScooterTestData as SD
import pytest
from endpoints.create_courier_object import CreateCourier
from endpoints.login_courier_object import LoginCourier
from faker import Faker
import allure

fake = Faker()


class TestCourierLogin:

    @allure.title('Проверка, что курьер может авторизоваться')
    def test_courier_successful_auth(self, fake_courier_required_fields):
        lc = LoginCourier()
        lc.courier_login(data=SD.FAKE_COURIER_CREATION_ONLY_REQUIRED_FIELDS)
        lc.status_code_and_name(200, 'id')


    @allure.title('Проверка ошибки при авторизации с пустым полем')
    @pytest.mark.parametrize("login, password", [(fake.user_name(), ""), ("", fake.password())])
    def test_courier_login_one_missed_field(self, login, password):
        lc = LoginCourier()
        lc.courier_login(data={'login': login, 'password': password})
        lc.check_status_code_and_text(400, 'message', 'Недостаточно данных для входа')

    @allure.title('Проверка ошибки при авторизации с несуществующим курьером')
    def test_non_existent_courier_login_failed(self):
        lc = LoginCourier()
        lc.courier_login(data={'login': fake.user_name(), 'password': fake.password})
        lc.check_status_code_and_text(404, 'message', 'Учетная запись не найдена')

    @allure.title('Проверка ошибки при авторизации с неверным полем логин')
    def test_courier_auth_login_field_wrong(self, fake_courier_required_login_password):
        login = fake_courier_required_login_password
        lc = LoginCourier()
        lc.courier_login(data={'login': login, 'password': '23432'})
        lc.check_status_code_and_text(404, 'message', 'Учетная запись не найдена')

    @allure.title('Проверка ошибки при авторизации с неверным полем пароль')
    def test_courier_auth_password_field_wrong(self, fake_courier_required_login_password):
        login = fake_courier_required_login_password
        lc = LoginCourier()
        lc.courier_login(data={'login': login, 'password': '23432'})
        lc.check_status_code_and_text(404, 'message', 'Учетная запись не найдена')
