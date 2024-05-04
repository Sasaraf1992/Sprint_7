import allure

import requests
import settings
from endpoints.base_object import BaseObject


class CreateOrder(BaseObject):
    @allure.step('Создание заказа')
    def order_creation(self, data):
        self.response = requests.post(settings.URL_ORDER_CREATION, json=data)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code

    @allure.step('Получение списка заказов')
    def get_order_list(self):
        self.response = requests.get(settings.URL_ORDER_LIST)
        self.response_json = self.response.json()
        self.response_status_code = self.response.status_code
