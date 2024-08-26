import zipfile
import os

def zip_file(file_path, part_size):
    with zipfile.ZipFile(f"{file_path}.zip", 'w') as zipf:
        zipf.write(file_path)
    
    zip_size = os.path.getsize(f"{file_path}.zip")
    if zip_size > part_size:
        with open(f"{file_path}.zip", 'rb') as f:
            part_num = 0
            while True:
                chunk = f.read(part_size)
                if not chunk:
                    break
                with open(f"{file_path}.part{part_num}", 'wb') as part_file:
                    part_file.write(chunk)
                part_num += 1

def unzip_file(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(os.path.dirname(zip_path))