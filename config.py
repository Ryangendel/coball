import os
currentDirectory = os.path.dirname(__file__)
class Config(object):
    DEBUG = True
    # SERVER_NAME ='localhost'
    DATABASE_URL = f'sqlite:///{ os.path.join(currentDirectory,"./testDatabase.db") }'
    ADMIN_MAIL_LIST = ['shawn-hartley@sbcglobal.net','gendel.ryan@gmail.com']
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = '465'
    # MAIL_USE_TLS = 'False'
    MAIL_USE_SSL = 'True'
    MAIL_USERNAME = 'coballsystems@gmail.com'
    MAIL_PASSWORD = 'c0b@11$y$t3ms'

class Development(Config):
    pass

class Qa(Config):
    pass

class Production(Config):
    DEBUG = False
    DATABASE_URL = 'postgres://iuhpxmphwetgmb:6dac26780c25f010c474c12973f76014d6f309eb2085f37cdb43eeafc1da9bfc@ec2-52-202-146-43.compute-1.amazonaws.com:5432/dc55qk2dqth8s7'
    # SERVER_NAME ='prod'
