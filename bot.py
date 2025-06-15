import requests
import configparser

config = configparser.ConfigParser()  # создаём объекта парсера
config.read("settings.ini")  # читаем конфиг
APIKey = config["APITelegram"]["key"] # обращаемся как к обычному словарю!
ChatId = config["APITelegram"]["ChatId"]

def sendMessage(message_text):

    send_message_url = f'https://api.telegram.org/bot{APIKey}/sendMessage'
                         
    payload = {
        'chat_id': ChatId,
         'text': message_text
    }
                         
    response = requests.post(send_message_url, data=payload)
