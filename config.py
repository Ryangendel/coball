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
    DATABASE_URL = 'postgres://iuhpxmphwetgmb:6dac26780c25f010c474c12973f76014d6f309eb2085f37cdb43eeafc1da9bfc@ec2-52-202-146-43.compute-1.amazonaws.com:5432/dc55qk2dqth8s7'
    # SERVER_NAME ='prod'
    SMTP_HOST = 'prod'
    SMTP_PORT = 'prod'
    MAIL_USER = 'prod'
    MAIL_USER_PW = 'prod'