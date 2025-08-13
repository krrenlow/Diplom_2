import allure
import data
import helpers
from methods.user_methods import UserMethods


@allure.story('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_user(self):
        payload = helpers.user_data
        user_response = UserMethods.create_user(payload)
        assert user_response[0]['success'] is True and user_response[1] == 200
        token = user_response[0]["accessToken"]
        UserMethods.delete_user(token)

    @allure.title('Создание пользователя, который уже зарегистрирован')
    def test_create_user_with_existing_data(self):
        payload = data.EXISTING_USER
        user_response = UserMethods.create_user(payload)
        assert user_response[0]['message'] == "User already exists" and user_response[1] == 403

    @allure.title('Создание пользователя без заполнения одного из обязательных полей')
    def test_create_user_with_wrong_data(self):
        payload = data.INVALID_USER_DATA
        user_response = UserMethods.create_user(payload)
        assert user_response[0]['message'] == "Email, password and name are required fields" and user_response[1] == 403