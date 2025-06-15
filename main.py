import psutil
import configparser
from bot import sendMessage
from time import sleep

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг
SignalProcent = int(config["InfoDisk"]["SignalProcent"])
TimeOut = int(config["APITelegram"]["TimeOutSendMessage"])

def check_free_space():
    # Получаем информацию о диске
    disk_usage = psutil.disk_usage("/")  # "/" - корневой раздел
    total_bytes = disk_usage.total
    # used_bytes = disk_usage.used
    free_bytes = disk_usage.free

    free_procent = round(free_bytes * 100 / total_bytes, 0)

    if free_procent <= SignalProcent:
        sendMessage(f"На диске осталось {free_procent}%")

while True:
    check_free_space()
    sleep(TimeOut)