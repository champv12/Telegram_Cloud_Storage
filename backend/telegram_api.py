import requests
from config import TELEGRAM_API_URL

def setup_telegram(api_key):
    url = f"{TELEGRAM_API_URL}/bot{api_key}/getUpdates"
    response = requests.get(url)
    return response.json()

def upload_to_telegram(file_path, api_key, chat_id):
    url = f"{TELEGRAM_API_URL}/bot{api_key}/sendDocument"
    with open(file_path, 'rb') as file:
        response = requests.post(url, data={'chat_id': chat_id}, files={'document': file})
    return response.json()

def download_from_telegram(file_id, api_key, chat_id):
    url = f"{TELEGRAM_API_URL}/bot{api_key}/getFile"
    response = requests.get(url, params={'file_id': file_id})
    file_path = response.json()['result']['file_path']
    download_url = f"{TELEGRAM_API_URL}/file/bot{api_key}/{file_path}"
    return requests.get(download_url)