import requests
from config import Config

def setup_telegram():
    config = Config.from_env()
    url = f"{config.telegram_api_url}/bot{config.api_key}/getUpdates"
    response = requests.get(url)
    return response.json()

def upload_to_telegram(file_path):
    config = Config.from_env()
    url = f"{config.telegram_api_url}/bot{config.api_key}/sendDocument"
    with open(file_path, 'rb') as file:
        response = requests.post(url, data={'chat_id': config.chat_id}, files={'document': file})
    return response.json()

def download_from_telegram(file_id):
    config = Config.from_env()
    url = f"{config.telegram_api_url}/bot{config.api_key}/getFile"
    response = requests.get(url, params={'file_id': file_id})
    file_path = response.json()['result']['file_path']
    download_url = f"{config.telegram_api_url}/file/bot{config.api_key}/{file_path}"
    return requests.get(download_url)

# Example usage
if __name__ == "__main__":
    # Setup Telegram
    updates = setup_telegram()
    print(updates)

    # Upload a file to Telegram
    upload_response = upload_to_telegram('path/to/your/file.txt')
    print(upload_response)

    # Download a file from Telegram
    file_id = 'your_file_id_here'
    download_response = download_from_telegram(file_id)
    with open('downloaded_file.txt', 'wb') as f:
        f.write(download_response.content)
    print("File downloaded successfully.")
