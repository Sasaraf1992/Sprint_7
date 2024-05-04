import allure

from endpoints.create_order_object import CreateOrder


class TestOrderList:

    @allure.title('Проверка успешного получения списка заказов')
    def test_successful_get_order_list(self):
        co = CreateOrder()
        co.get_order_list()
        co.status_code_and_name(200, 'orders')
