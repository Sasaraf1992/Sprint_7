import allure

import requests
import settings
from endpoints.base_object import BaseObject


class LoginCourier(BaseObject):

    @allure.step("Логин курьера в систему")
    def courier_login(self, data):
        self.response = requests.post(settings.URL_COURIER_LOGIN, data)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code
