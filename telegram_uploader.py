import requests
from config import Config

def upload_chunk(file_path):
    url = f'https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendDocument'
    with open(file_path, 'rb') as f:
        files = {'document': f}
        params = {'chat_id': Config.TELEGRAM_CHAT_ID}
        response = requests.post(url, files=files, data=params)
    return response

def upload_chunks(chunk_list):
    for chunk in chunk_list:
        response = upload_chunk(chunk)
        if response.status_code == 200:
            print(f'Successfully uploaded {chunk}')
        else:
            print(f'Failed to upload {chunk}: {response.text}')