from dotenv import load_dotenv
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Загрузить переменные окружения из файла .env
load_dotenv()

# Использовать переменные окружения
USER_NAME_SHAFA = os.getenv('USER_NAME_SHAFA')
PASSWORD_SHAFA = os.getenv('PASSWORD_SHAFA')

TELEGRAM_APP_API_ID = os.getenv('TELEGRAM_APP_API_ID')
TELEGRAM_APP_API_HASH = os.getenv('TELEGRAM_APP_API_HASH')
TELEGRAM_APP_TITLE = os.getenv('TELEGRAM_APP_TITLE')
TELEGRAM_SHORT_NAME = os.getenv('TELEGRAM_SHORT_NAME')

CHANNEL_URL = 'https://t.me/onlydrop2'

PATH_TO_MEDIA_FOLDER = os.path.abspath(os.path.join('..', 'media'))

MARGIN = 45
