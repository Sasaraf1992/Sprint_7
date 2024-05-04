import requests
import settings
from data import ScooterTestData as SD
from faker import Faker
import pytest

fake = Faker()


class TestCourier:
    def test_courier_successful_creation(self):
        response = requests.post(settings.URL_COURIER_CREATION, data=SD.COURIER_CREATION)
        assert response.status_code == 201 and response.json()["ok"] == True

    def test_courier_duplicate_creation_failed(self):
        response = requests.post(settings.URL_COURIER_CREATION, data=SD.COURIER_CREATION)
        response = requests.post(settings.URL_COURIER_CREATION, data=SD.COURIER_CREATION)

        assert response.status_code == 409 and response.json()["message"] == "Этот логин уже используется"

    def test_courier_required_fields_only(self):
        response = requests.post(settings.URL_COURIER_CREATION, data=SD.COURIER_CREATION_ONLY_REQUIRED_FIELDS)
        assert response.status_code == 201 and response.json()['ok'] == True

    @pytest.mark.parametrize("login, password", [(fake.user_name(), None), (None, fake.password())])
    def test_courier_required_fields_one_missed_fail(self, login, password):
        response = requests.post(settings.URL_COURIER_CREATION, data={"login": login, "password": password})
        assert response.status_code == 400 and response.json()["message"] == ("Недостаточно данных для создания "
                                                                              "учетной записи")
