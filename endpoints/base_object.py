import allure


class BaseObject:
    response = None
    response_json = None
    response_status_code = None

    @allure.step('Проверка статуса и текста')
    def check_status_code_and_text(self, code, name, text):
        assert self.response_status_code == code and self.response_json[name] == text

    @allure.step('Проверка статуса и ключа')
    def status_code_and_name(self, code, name):
        assert self.response_status_code == code and name in self.response_json

