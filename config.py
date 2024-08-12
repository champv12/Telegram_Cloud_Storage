import os

class Config:
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', 'your-default-bot-token')
    TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID', 'your-default-chat-id')
    CHUNK_SIZE = 50 * 1024 * 1024# 50MB
    UPLOAD_DIR = os.path.join(os.getcwd(), 'uploads')
    INDEX_FILE = os.path.join(UPLOAD_DIR, 'file_index.txt')

# Create the upload directory if it doesn't existif not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)