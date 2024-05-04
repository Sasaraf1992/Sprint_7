import requests
import settings
from data import ScooterTestData as SD
from faker import Faker
import pytest

fake = Faker()


class TestCourierLogin:

    def test_courier_successful_auth(self):
        response = requests.post(settings.URL_COURIER_LOGIN, data = SD.TRUE_COURIER)
        assert response.status_code == 200 and response.json()['id'] == 296745

    @pytest.mark.parametrize("login, password", [('Sasaraf', None), (None, '1234')])
    def test_courier_auth_one_field_miss(self, login, password):
        response = requests.post(settings.URL_COURIER_LOGIN, data={'login': login, 'password': password})
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    def test_non_existent_courier_login_failed(self):
        response = requests.post(settings.URL_COURIER_LOGIN, data=SD.FAKE_COURIER_CREATION_ONLY_REQUIRED_FIELDS)
        assert response.status_code == 404, response.json()['message'] == "Учетная запись не найдена"

