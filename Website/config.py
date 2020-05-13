class Config(object):
    DEBUG = True
    DATABASE_URI = 'sqlite:///C:\\Users\\NT_WIN10\\Desktop\\Coball\\Website\\testDatabase.db'
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
    DATABASE_URI = 'prod'
    SMTP_HOST = 'prod'
    SMTP_PORT = 'prod'
    MAIL_USER = 'prod'
    MAIL_USER_PW = 'prod'