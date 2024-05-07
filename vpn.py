import subprocess
import time

def connect_vpn(server_address, username, password):
    """Функция для подключения к VPN серверу"""
    vpncli_path = 'C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpncli.exe'
    
    # Запуск процесса подключения
    process = subprocess.Popen([vpncli_path, 'connect', server_address],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Отправка учетных данных
    process.stdin.write(username + '\n')
    time.sleep(1)  # Небольшая задержка для корректной обработки ввода
    process.stdin.write(password + '\n')

    
    # Получение вывода процесса
    output, error = process.communicate()
    print(output)
    if "Connected" in output:
        print(f"Успешно подключено к {server_address}")
    else:
        print(f"Ошибка подключения к {server_address}")

def disconnect_vpn():
    """Функция для отключения от VPN"""
    vpncli_path = 'C:\\Program Files (x86)\\Cisco\\Cisco AnyConnect Secure Mobility Client\\vpncli.exe'
    process = subprocess.Popen([vpncli_path, 'disconnect'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Получение вывода процесса
    output, error = process.communicate()
    print(output)
    if "Disconnected" in output:
        print("Успешно отключено от VPN")
    else:
        print("Ошибка отключения от VPN")

if __name__ == "__main__":
    servers = ['vpngw2.lureit.ru', 'vpngw.cds-co.ru']  # Список серверов VPN
    username = 'mramishvili'
    password = input(f"Введите пароль для подключения к {'server_address'}: ")


    for server in servers:
        print(f"Подключение к {server}")
        connect_vpn(server, username, password)
        time.sleep(10)  # Поддерживаем подключение в течение 10 секунд
        disconnect_vpn()
        time.sleep(5)  # Пауза перед следующим подключением
