import allure
import helpers
from methods.user_methods import UserMethods


@allure.story('Изменение данных пользователя')
class TestChangeUserData:

    @allure.title('Изменение данных пользователя с авторизацией')
    def test_change_authorized_user_data(self):
        new_payload = helpers.create_user_data()
        payload = helpers.user_data
        UserMethods.create_user(payload)
        response = UserMethods.login_user(payload)
        access_token = response[0]['accessToken']
        user_response = UserMethods.change_authorized_user_data(new_payload, access_token)
        assert user_response == 200
        UserMethods.delete_user(access_token)

    @allure.title('Изменение данных пользователя без авторизации')
    def test_change_non_authorized_user_data(self):
        new_payload = helpers.create_user_data()
        payload = helpers.user_data
        UserMethods.create_user(payload)
        token_response = UserMethods.login_user(payload)
        user_response = UserMethods.change_non_authorized_user_data(new_payload)
        assert user_response[0]['message'] == "You should be authorised" and user_response[1] == 401
        token = token_response[0]["accessToken"]
        UserMethods.delete_user(token)