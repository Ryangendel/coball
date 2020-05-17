import smtplib,ssl
from baseApp import app

smtpHost = app.config["SMTP_HOST"]
smtpPort = app.config["SMTP_PORT"]
mailUserName = app.config["MAIL_USER"]
mailUserPW = app.config["MAIL_USER_PW"]

sslContext = ssl.create_default_context()


# message = """From: From Person <from@fromdomain.com>
# To: To Person <to@todomain.com>
# MIME-Version: 1.0
# Content-type: text/html
# Subject: SMTP HTML e-mail test

# This is an e-mail message to be sent in HTML format

# <b>This is HTML message.</b>
# <h1>This is headline.</h1>
# """
# from flask_mail import Mail,Message
# class Message():
#     def __init__(self,sender: str = "No-Reply@website.com", receiver: list = app.config["ADMIN_MAIL_LIST"], message: str = None) -> None:
#         self.sender = sender
#         self.receiver = receiver
#         self.message = message
        

# class Mailer():
#     def __init__(self) -> None:
#         self.smtpHost = smtpHost
#         self.smtpPort = smtpPort
    
#     def sendMail(self,message: Message) -> bool:
#         try:
#             with smtplib.SMTP_SSL(self.smtpHost, self.smtpPort, context=sslContext) as server:
#                 server.login(mailUserName, mailUserPW)
#                 for recipients in message.receiver:
#                     server.sendmail(message.sender,message.receiver,message.message)
#             return True
#         except Exception as e:
#             print(e)
#             return False

# mail_settings = {
#     "MAIL_SERVER": app.config['SMTP_HOST'],
#     "MAIL_PORT": app.config['SMTP_PORT'],
#     "MAIL_USE_TLS": False,
#     "MAIL_USE_SSL": True,
#     "MAIL_USERNAME": app.config['MAIL_USER'],
#     "MAIL_PASSWORD": app.config['MAIL_USER_PW']
# }