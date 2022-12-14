from typing import Any
import telebot
from decouple import config as conf_token
from sys import argv
import os
import json


def send_m(message: str = 'Привет, мир', id: str = '', bot: Any = None) -> None:
    """
    функция отправки сообщения в телеграм
    :param message: str текст сообщения
    :param id: str id чата в который отправляем
    :param bot: object объект бота телеграм для отправки
    :return: None
    """
    bot.send_message(id, '<b>{}</b>'.format(message), parse_mode='html')


def make_dict_message(f_name: str = 'message.json', f_path: str = 'r:\\') -> dict:
    full_path = os.path.normpath(f_path + '\\' + f_name)
    data = {}
    if os.path.exists(full_path):
        with open(full_path, 'r', encoding='cp1251') as j_file:
            data = json.load(j_file)
    return data


def make_message(i_dict: dict = {}) -> str:
    i_message = 'Магазин: {0} \nСообщение: {1} \nНомер чека: {2} \nСумма: {3} \nКод проверки {4}'.format(
        i_dict.get("shop", "TT"), i_dict.get("text", "заглушка"),
        i_dict.get("number", "нет номера"), i_dict.get("summ", "нет суммы"),
        i_dict.get("code", ""))
    return i_message


def main():
    """
    функция для отправки одноразовых паролей в телеграмм
    задумана как замена нашим смc для повторов чека,
    возвратов сертификата, чеков коррекции и прочих
    операций что требуют повышения прав у кассиров
    :return:
    """
    os.chdir('d:\\kassa\\script_py\\telegram_send_code\\')
    token = conf_token('token', default=None)
    id = conf_token('id', default=None)
    bot = telebot.TeleBot(token)
    dict_message = make_dict_message(f_path=argv[1], f_name=argv[2])
    message = make_message(i_dict=dict_message)
    send_m(message=message, id=id, bot=bot)


if __name__ == '__main__':
    main()
