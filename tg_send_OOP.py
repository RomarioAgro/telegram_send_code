from typing import Any
import telebot
from decouple import config as conf_token
from sys import argv
import os
import json
from pathlib import Path

from dotenv import load_dotenv
BASE_DIR = Path(__file__).resolve().parent
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)


def make_message(i_dict: dict = {}):
    message = 'Магазин: {0} \nСообщение: {1} \nНомер чека: {2} \nСумма: {3} \nКод проверки {4}'.format(
        i_dict.get("shop", "TT"), i_dict.get("text", "заглушка"),
        i_dict.get("number", "нет номера"), i_dict.get("summ", "нет суммы"),
        i_dict.get("code", ""))
    return message


class TgSender:

    def __init__(self, message: dict = {}):
        # load_dotenv('d:\\kassa\\script_py\\telegram_send_code\\.env')
        # self.token = conf_token('token', default=None)
        self.token = os.getenv('token')
        # self.id = conf_token('id', default=None)
        self.id = os.getenv('id')
        self.bot = telebot.TeleBot(self.token)
        self.message = make_message(i_dict=message)

    def send_message(self):
        self.bot.send_message(self.id, '<b>{}</b>'.format(self.message), parse_mode='html')


def main():
    """
    функция для отправки одноразовых паролей в телеграмм
    задумана как замена нашим смc для повторов чека,
    возвратов сертификата, чеков коррекции и прочих
    операций что требуют повышения прав у кассиров
    :return:
    """
    my_dict = {
        'shop': 'C85',
        'text': 'тестовый текст'
    }
    my_bot = TgSender(message=my_dict)
    my_bot.send_message()


if __name__ == '__main__':
    main()
