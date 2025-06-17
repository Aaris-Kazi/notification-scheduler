from config import ConfigReader
from dotenv import load_dotenv

load_dotenv()
configfile = ConfigReader('src/run/etc.xml')
TAG = "notification_service"

SECRET_KEY = configfile.getProperty(TAG + ".django_cred_token")
DEBUG = configfile.getProperty(TAG + ".debug") == "true"
ALLOWED_HOSTS = configfile.getProperty(TAG + ".cors_list").split("\\s*,\\s*")

REDIS_DB = configfile.getProperty(TAG + ".redis_db")
REDIS_HOST = configfile.getProperty(TAG + ".redis_host")
REDIS_PORT = configfile.getProperty(TAG + ".redis_port")


