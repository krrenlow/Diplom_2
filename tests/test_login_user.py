import allure
import data
import helpers
from methods.user_methods import UserMethods


@allure.story('Логин пользователя')
class TestLoginUser:

    @allure.title('Логин под существующим пользователем')
    def test_login_user(self):
        payload = helpers.user_data
        UserMethods.create_user(payload)
        user_response = UserMethods.login_user(payload)
        assert user_response[0]['success'] is True and user_response[1] == 200
        token = user_response[0]["accessToken"]
        UserMethods.delete_user(token)

    @allure.title('Логин с неверным логином и паролем')
    def test_login_user_with_wrong_data(self):
        payload = data.INVALID_USER_DATA
        user_response = UserMethods.login_user(payload)
        assert user_response[0]['message'] == "email or password are incorrect" and user_response[1] == 401