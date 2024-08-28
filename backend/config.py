from flask import request
import os

class Config:
    def __init__(self):
        self.user_id = self.get_request_arg('user_id')
        self.api_key = self.get_request_arg('api_key')
        self.chat_id = self.get_request_arg('chat_id')
        self.telegram_api_url = self.get_request_arg('telegram_api_url')
        self.telegram_api_id = self.get_request_arg('telegram_api_id')
        self.telegram_api_hash = self.get_request_arg('telegram_api_hash')

    def get_request_arg(self, arg_name):
        value = request.args.get(arg_name)
        if not value:
            raise ValueError(f"Missing required parameter: {arg_name}")
        return value

    @staticmethod
    def from_env():
        config = Config()
        config.user_id = os.getenv('USER_ID', config.user_id)
        config.api_key = os.getenv('API_KEY', config.api_key)
        config.chat_id = os.getenv('CHAT_ID', config.chat_id)
        config.telegram_api_url = os.getenv('TELEGRAM_API_URL', config.telegram_api_url)
        config.telegram_api_id = os.getenv('TELEGRAM_API_ID', config.telegram_api_id)
        config.telegram_api_hash = os.getenv('TELEGRAM_API_HASH', config.telegram_api_hash)
        return config

# Example usage
if __name__ == '__main__':
    config = Config.from_env()
    print(f"User ID: {config.user_id}")
    print(f"API Key: {config.api_key}")
    print(f"Chat ID: {config.chat_id}")
    print(f"Telegram API URL: {config.telegram_api_url}")
    print(f"Telegram API ID: {config.telegram_api_id}")
    print(f"Telegram API Hash: {config.telegram_api_hash}")
