import os
import zipfile
from config import Config

def split_file(file_path):
    base_name = os.path.basename(file_path)
    chunks = []

    chunk_size = Config.CHUNK_SIZE
    with open(file_path, 'rb') as f:
        chunk_counter = 0
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            chunk_file_name = os.path.join(Config.UPLOAD_DIR, f"{base_name}.part{chunk_counter}")
            with open(chunk_file_name, 'wb') as chunk_file:
                chunk_file.write(chunk)
            chunks.append(chunk_file_name)
            chunk_counter += 1

    save_index(chunks)
    return chunks

def save_index(file_list):
    with open(Config.INDEX_FILE, 'w') as f:
        for file in file_list:
            f.write(file + '\n')

def unzip_file(zip_path, target_dir):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(target_dir)
    return {"message": "File unzipped successfully!"}