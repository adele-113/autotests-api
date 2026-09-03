import socket
import threading

# ГЛОБАЛЬНЫЙ СПИСОК для хранения ВСЕЙ истории сообщений
messages = []
MAX_CONNECTIONS = 10


def handle_client(client_socket, client_address):
    """
    Обрабатывает одного клиента в отдельном потоке.
    """
    print(f"Пользователь с адресом: {client_address} подключился к серверу")

    try:
        while True:
            # 1. Ожидание сообщения от клиента
            data = client_socket.recv(1024)
            if not data:
                # Клиент сам отключился
                break

            message = data.decode('utf-8')

            # 2. Логирование и добавление в историю
            print(f"{message}")

            # Добавление нового сообщения в общий список
            history_entry = f"{message}"
            messages.append(history_entry)

            # 3. Отправка клиенту ВСЕЙ истории сообщений
            response_message = "\n".join(messages).encode('utf-8')
            client_socket.sendall(response_message)

    finally:
        # Закрытие соединения
        client_socket.close()
        print(f"Пользователь с адресом {client_address} отключился.")


def server():
    # Создание TCP-сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязка к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Начинаем слушать входящие подключения (максимум 10 в очереди)
    server_socket.listen(MAX_CONNECTIONS)
    print(f"Сервер TCP запущен на {server_address} и ждет подключений...")

    try:
        while True:
            # Принимаем новое подключение (БЛОКИРУЕТ)
            client_socket, client_address = server_socket.accept()

            # Запуск обработки в новом потоке (для параллельности)
            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.start()

    except KeyboardInterrupt:
        print("\nСервер остановлен пользователем.")
    finally:
        server_socket.close()


if __name__ == "__main__":
    server()