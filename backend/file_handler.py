import os
import logging
from utils.zip_utils import zip_file, unzip_file
from telegram_utils import upload_to_telegram, download_from_telegram
from config import UPLOAD_LIMIT

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_upload(file, user_id, api_key, chat_id):
    try:
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)
        logger.info(f"File saved to {file_path}")

        if os.path.getsize(file_path) > UPLOAD_LIMIT:
            zip_file(file_path, UPLOAD_LIMIT)
            parts = [f"{file_path}.part{i}" for i in range(len(os.listdir('/tmp')))]
            logger.info(f"File split into parts: {parts}")
        else:
            parts = [file_path]

        responses = []
        for part in parts:
            response = upload_to_telegram(part, api_key, chat_id)
            responses.append(response)
            logger.info(f"Uploaded part {part} with response {response}")

        return responses

    except Exception as e:
        logger.error(f"Error during file upload: {e}")
        raise

def handle_download(file_id, user_id, api_key, chat_id):
    try:
        response = download_from_telegram(file_id, api_key, chat_id)
        file_path = f"/tmp/{file_id}"
        with open(file_path, 'wb') as file:
            file.write(response.content)
        logger.info(f"File downloaded to {file_path}")

        unzip_file(file_path)
        logger.info(f"File unzipped at {file_path}")

        return {"status": "success"}

    except Exception as e:
        logger.error(f"Error during file download: {e}")
        raise
