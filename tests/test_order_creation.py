import allure

from data import ScooterTestData as SD
import pytest
from endpoints.create_order_object import CreateOrder


class TestOrderCreation:
    @allure.title('Проверка создания заказа с мопедами разных цветов')
    @pytest.mark.parametrize('color', ["BLACK", "GREY", ["BLACK", "GREY"], None])
    def test_successful_order_creation_scooter_color(self, color):
        co = CreateOrder()
        payload = SD.SCOOTER_ORDER_DATA.copy()
        payload['color'] = [color]
        co.order_creation(payload)
        co.status_code_and_name(201, 'track')
