class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    USER_URL = f"{BASE_URL}/api/auth/user"
    REGISTRATION_URL = f"{BASE_URL}/api/auth/register"
    LOGIN_URL = f"{BASE_URL}/api/auth/login"
    ORDER_URL = f"{BASE_URL}/api/orders/all"
    USER_ORDERS_URL = f"{BASE_URL}/api/orders"
    INGREDIENTS_URL = f"{BASE_URL}/api/ingredients"


EXISTING_USER = {
    "email": "test-data@yandex.ru",
    "password": "password",
    "name": "Username"
}

INVALID_USER_DATA = {
    "email": "test-data@yandex.ru",
    "password": "",
    "name": ""
}

INGREDIENTS = {
    "ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6f"]
}

EMPTY_INGREDIENTS = {
    "ingredients": []
}

WRONG_INGREDIENTS = {
    "ingredients": ["61c0c5a7qwe1d1f82001bdaaa6d", "61c0c5a7qwe1d1f82001bdaaa6f"]
}