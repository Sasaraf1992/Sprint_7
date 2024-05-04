import allure

import requests
import settings
from endpoints.base_object import BaseObject


class CreateCourier(BaseObject):

    @allure.step('Создание курьера')
    def courier_creation(self, data):
        self.response = requests.post(settings.URL_COURIER_CREATION, data)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code

