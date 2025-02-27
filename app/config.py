import os
from dotenv import load_dotenv
import base64

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = True

    print("Loading environment variables...")

    print(os.environ.get('SECRET_KEY', 'Som3$ec5etK*y'))
    print(os.environ.get('MAIL_SERVER', 'localhost'))
    print(os.environ.get('MAIL_PORT', '25'))
    print(os.environ.get('MAIL_USERNAME'))
    print(os.environ.get('MAIL_PASSWORD'))
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y') 
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'localhost') 
    MAIL_PORT = os.environ.get('MAIL_PORT', '25') 
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') 
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

   
    print("Server:", MAIL_SERVER)
    print("Port:", MAIL_PORT)
    print("Username:", MAIL_USERNAME)
    print("Password:", MAIL_PASSWORD)
    print("Secret Key:", SECRET_KEY)


