import httpx #импортируем библиотеку HTTPX

#данные для входа в систему

login_payload = {
    "email": "test_user@test.com",
    "password": "123qwe",
}

#Выполняем  запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

#выводим полученные токены
print("Login response:", login_response_data)
print("Status code:", login_response.status_code)

#формируем payload для обновления токена
refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

#выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8000/api/v1/authentication/refresh",json=refresh_payload)
refresh_response_data = refresh_response.json()

#выводим обновленные токены
print("Refresh response:", refresh_response_data)
print("Status code:", refresh_response.status_code)