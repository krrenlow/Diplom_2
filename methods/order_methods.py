import allure
import requests
from data import Urls


class OrderMethods:
    @staticmethod
    @allure.step('Создание заказа без авторизации')
    def create_order_without_auth(payload):
        response = requests.post(Urls.USER_ORDERS_URL, data=payload)
        return response.status_code

    @staticmethod
    @allure.step('Создание заказа')
    def create_order(payload, auth_key):
        response = requests.post(Urls.USER_ORDERS_URL, data=payload, headers={'Authorization': f"{auth_key}"})
        return response.status_code

    @staticmethod
    @allure.step('Получение заказа авторизованного пользователя')
    def get_orders_user(auth_key):
        response = requests.get(Urls.USER_ORDERS_URL, headers={'Authorization': f"{auth_key}"})
        return response.json(), response.status_code

    @staticmethod
    @allure.step('Получение заказа неавторизованного пользователя')
    def get_orders_user_without_auth():
        response = requests.get(Urls.USER_ORDERS_URL)
        return response.json(), response.status_code