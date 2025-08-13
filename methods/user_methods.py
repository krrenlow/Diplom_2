import allure
import requests
from data import Urls


class UserMethods:
    @staticmethod
    @allure.step('Создание пользователя')
    def create_user(payload):
        response = requests.post(Urls.REGISTRATION_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    @allure.step('Логин пользователя')
    def login_user(payload):
        response = requests.post(Urls.LOGIN_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    @allure.step('Изменение данных пользователя')
    def change_authorized_user_data(payload, auth_key):
        response = requests.patch(Urls.USER_URL, data=payload, headers={'Authorization': f"{auth_key}"})
        return response.status_code

    @staticmethod
    @allure.step('Изменение данных пользователя без авторизации')
    def change_non_authorized_user_data(payload):
        response = requests.patch(Urls.USER_URL, data=payload)
        return response.json(), response.status_code

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete_user(token):
        response = requests.delete(Urls.USER_URL, headers={'Authorization': f"{token}"})
        return response.status_code