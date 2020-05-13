import os
currentDirectory = os.path.dirname(__file__)
class Config(object):
    DEBUG = True
    # SERVER_NAME ='localhost'
    DATABASE_URL = f'sqlite:///{ os.path.join(currentDirectory,"./testDatabase.db") }'
    SMTP_HOST = ''
    SMTP_PORT = ''
    MAIL_USER = ''
    MAIL_USER_PW = ''
    ADMIN_MAIL_LIST = ['shawn-hartley@sbcglobal.net','gendel.ryan@gmail.com']

class Development(Config):
    pass

class Qa(Config):
    pass

class Production(Config):
    DEBUG = False
    DATABASE_URL = 'prod'
    # SERVER_NAME ='prod'
    SMTP_HOST = 'prod'
    SMTP_PORT = 'prod'
    MAIL_USER = 'prod'
    MAIL_USER_PW = 'prod'