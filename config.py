import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'pS^jS%oz)7$dVYa9DkheoRR7oNxCrmd43UDX3eg)KR4Rc$^J9h'
