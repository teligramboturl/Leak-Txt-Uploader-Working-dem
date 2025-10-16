# config.py
import os

# Bot Configuration
BOT_NAME = os.environ.get('BOT_NAME', 'palsab')
BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
API_ID = int(os.environ.get('API_ID', ''))
API_HASH = os.environ.get('API_HASH', '')
MONGO_URI = os.environ.get('MONGO_URI', '')

# Additional Configuration
OWNER_ID = int(os.environ.get('OWNER_ID', ''))
LOG_CHANNEL_ID = int(os.environ.get('LOG_CHANNEL_ID', ''))


