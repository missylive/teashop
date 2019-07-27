import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'qwertyuiopasdfghjkl'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'mysql://teashop:1qa!QA2ws@WS3ed#ED4rf$RF@localhost/teashop')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
