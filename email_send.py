import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from sys import argv
import os

def main():
    # отправка почты с итогами оптимизации базы данных сбис в рознице
    msg = MIMEMultipart()
    msg['From'] = 'sbis@gl.local'
    msg['To'] = 'it@acewear.ru'
    msg['Subject'] = argv[1]

    # Добавление вложения
    path_to_file = 'd:\\kassa\\JINNEE\\JINNEE.LOG'
    if os.path.exists(path_to_file):
        with open(path_to_file, 'rb') as f:
            attachment = MIMEApplication(f.read(), _subtype='txt')
            attachment.add_header('Content-Disposition', 'attachment', filename='JINNEE.LOG')
            msg.attach(attachment)
    # Отправка сообщения
    with smtplib.SMTP('mail.gl.local') as smtp:
        smtp.send_message(msg)


if __name__ == '__main__':
    main()
