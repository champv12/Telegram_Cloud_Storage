import requests
from config import TELEGRAM_API_URL

def send_message(api_key, chat_id, text):
    """
    Send a text message to a Telegram chat.
    
    :param api_key: The API key for the Telegram bot.
    :param chat_id: The chat ID to send the message to.
    :param text: The text message to send.
    :return: The response from the Telegram API.
    """
    url = f"{TELEGRAM_API_URL}/bot{api_key}/sendMessage"
    response = requests.post(url, data={'chat_id': chat_id, 'text': text})
    return response.json()

def get_updates(api_key):
    """
    Get updates from the Telegram bot.
    
    :param api_key: The API key for the Telegram bot.
    :return: The response from the Telegram API.
    """
    url = f"{TELEGRAM_API_URL}/bot{api_key}/getUpdates"
    response = requests.get(url)
    return response.json()

def get_file_info(api_key, file_id):
    """
    Get information about a file from Telegram.
    
    :param api_key: The API key for the Telegram bot.
    :param file_id: The file ID to get information about.
    :return: The response from the Telegram API.
    """
    url = f"{TELEGRAM_API_URL}/bot{api_key}/getFile"
    response = requests.get(url, params={'file_id': file_id})
    return response.json()

def download_file(api_key, file_path):
    """
    Download a file from Telegram.
    
    :param api_key: The API key for the Telegram bot.
    :param file_path: The file path to download.
    :return: The file content.
    """
    download_url = f"{TELEGRAM_API_URL}/file/bot{api_key}/{file_path}"
    response = requests.get(download_url)
    return response.content
