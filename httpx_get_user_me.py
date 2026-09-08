import httpx

login_payload = {
    "email": "test_user@test.com",
    "password": "123qwe"
}

#Выполняем  запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

#выводим полученные токены
print("Token:", login_response_data)

#задаем аксесс токен
ACCESS_TOKEN = login_response_data["token"]["accessToken"]

#задаем заголовок
headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

#выполняем запрос с аксесс токеном в заголовке
response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

#выводим результат в консоль
print("User:", response.json())
print("Status code:", response.status_code)