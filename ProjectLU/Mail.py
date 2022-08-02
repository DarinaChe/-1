import os
import smtplib
from email.mime.multipart import MIMEMultipart
import mimetypes
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

path13 = input('Введите расположение файла "Новая ЗП общая": ')


def mail(adress, path):
    addr_from = "darina86@inbox.ru"
    addr_to = adress
    password = "aeBnsQwae4ZLs8SGHTz4"

    msg = MIMEMultipart()  # Создаем сообщение
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = 'Зарплатный файл'

    body = "Добрый день. Зарплатный файл во вложении"
    msg.attach(MIMEText(body, 'plain'))

    filepath = path
    filename = os.path.basename(filepath)

    if os.path.isfile(filepath):
      ctype, encoding = mimetypes.guess_type(filepath)
      if ctype is None or encoding is not None:
          ctype = 'application/octet-stream'
      maintype, subtype = ctype.split('/', 1)
      if maintype == 'text':
          with open(filepath) as fp:
              file = MIMEText(fp.read(), _subtype=subtype)
              fp.close()
      else:
          with open(filepath, 'rb') as fp:
              file = MIMEBase(maintype, subtype)
              file.set_payload(fp.read())
              fp.close()
          encoders.encode_base64(file)
      file.add_header('Content-Disposition', 'attachment', filename=filename)
      msg.attach(file)


    server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()

    return print("Отправлено")

path133 =path13.partition('Новая ЗП общая.xlsx')[0]


mail("darina86@inbox.ru", f'{path133}{"Варламов.xlsx"}')