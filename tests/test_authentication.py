from http import HTTPStatus

from clients.authentication.authentication_client import get_authentication_client
from clients.authentication.authentication_schema import LoginResponseSchema, LoginRequestSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
# Импортируем функцию проверки ответа логина пользователя
from tools.assertions.authentication import assert_login_response
# Импортируем функцию для валидации JSON Schema
from tools.assertions.schema import validate_json_schema
# Импортируем функцию проверки статус-кода
from tools.assertions.base import assert_status_code



def test_login():
    # Инициализируем API-клиент для работы с пользователями
    public_users_client = get_public_users_client()
    public_authentication_client = get_authentication_client()
    # Формируем тело запроса на создание пользователя
    create_user_request = CreateUserRequestSchema()
    # Отправляем запрос на создание пользователя
    public_users_client.create_user_api(create_user_request)
    authentication_user = LoginRequestSchema(
        email=create_user_request.email,
        password=create_user_request.password
    )
    login_response = public_authentication_client.login_api(authentication_user)
    login_response_data = LoginResponseSchema.model_validate_json(login_response.text)
    # Используем функцию для проверки статус-кода
    assert_status_code(login_response.status_code, HTTPStatus.OK)
    # Используем функцию для проверки ответа логина пользователя
    assert_login_response(login_response_data)
    # Проверяем, что тело ответа соответствует ожидаемой JSON-схеме
    validate_json_schema(login_response.json(), login_response_data.model_json_schema())
