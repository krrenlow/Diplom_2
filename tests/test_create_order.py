import allure
import data
import helpers
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


@allure.story('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией')
    def test_create_order_with_auth(self):
        payload = helpers.user_data
        new_payload = data.INGREDIENTS
        user_response = UserMethods.create_user(payload)
        access_token = user_response[0]['accessToken']
        order_response = OrderMethods.create_order(new_payload, access_token)
        assert order_response == 200
        UserMethods.delete_user(access_token)

    @allure.title('Создание заказа без авторизации')
    def test_create_order_without_auth(self):
        payload = data.INGREDIENTS
        order_response = OrderMethods.create_order_without_auth(payload)
        assert order_response == 200

    @allure.title('Создание заказа с ингредиентами')
    def test_create_order_without_ingredients(self):
        payload = data.INGREDIENTS
        order_response = OrderMethods.create_order_without_auth(payload)
        assert order_response == 200

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self):
        payload = data.EMPTY_INGREDIENTS
        order_response = OrderMethods.create_order_without_auth(payload)
        assert order_response == 400

    @allure.title('Создание заказа с с неверным хешем ингредиентов')
    def test_create_order_with_wrong__hash_ingredients(self):
        payload = data.WRONG_INGREDIENTS
        order_response = OrderMethods.create_order_without_auth(payload)
        assert order_response == 500