import allure
import helpers
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


@allure.story('Получение заказов конкретного пользователя')
class TestGerOrdersUser:

    @allure.title('Получение заказов авторизованного пользователя')
    def test_get_orders_with_auth(self):
        payload = helpers.user_data
        user_response = UserMethods.create_user(payload)
        access_token = user_response[0]['accessToken']
        order_response = OrderMethods.get_orders_user(access_token)
        assert order_response[0]['success'] and order_response[1] == 200
        UserMethods.delete_user(access_token)

    @allure.title('Получение заказов неавторизованного пользователя')
    def test_get_orders_without_auth(self):
        order_response = OrderMethods.get_orders_user_without_auth()
        assert order_response[0]['message'] and order_response[1] == 401