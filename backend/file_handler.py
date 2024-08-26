import os
from utils.zip_utils import zip_file, unzip_file
from telegram_api import upload_to_telegram, download_from_telegram
from config import UPLOAD_LIMIT

def handle_upload(file, user_id, api_key, chat_id):
    file_path = f"/tmp/{file.filename}"
    file.save(file_path)
    
    if os.path.getsize(file_path) > UPLOAD_LIMIT:
        zip_file(file_path, UPLOAD_LIMIT)
        parts = [f"{file_path}.part{i}" for i in range(len(os.listdir('/tmp')))]
    else:
        parts = [file_path]
    
    responses = []
    for part in parts:
        response = upload_to_telegram(part, api_key, chat_id)
        responses.append(response)
    
    return responses

def handle_download(file_id, user_id, api_key, chat_id):
    response = download_from_telegram(file_id, api_key, chat_id)
    with open(f"/tmp/{file_id}", 'wb') as file:
        file.write(response.content)
    
    unzip_file(f"/tmp/{file_id}")
    return {"status": "success"}