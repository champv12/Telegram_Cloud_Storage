from flask import Flask, request, render_template, send_file, jsonify
from config import Config
from file_manager import unzip_file, split_file, save_index
from telegram_uploader import upload_chunks
import os

app = Flask(__name__)

@app.route('/')
def index():
    if os.path.exists(Config.INDEX_FILE):
        with open(Config.INDEX_FILE, 'r') as f:
            files = [line.strip() for line in f]
    else:
        files = []
    return render_template('index.html', files=files)

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    file_path = os.path.join(Config.UPLOAD_DIR, filename)
    if os.path.exists(file_path):
        return send_file(file_path, as_attachment=True)
    else:
        return "File not found", 404

@app.route('/unzip', methods=['POST'])
def unzip():
    zip_path = request.form['zip_file']
    target_dir = request.form['target_dir']

    if not os.path.exists(zip_path):
        return jsonify({"error": "Zip file not found"}), 404
    if not os.path.isdir(target_dir):
        return jsonify({"error": "Target directory not found"}), 404

    return jsonify(unzip_file(zip_path, target_dir))

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file_path = request.form['file_path']

    try:
# Split file into chunks
        chunks = split_file(file_path)

# Upload chunks to Telegram
        upload_chunks(chunks)

        return jsonify({"message": "File uploaded successfully!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    from gunicorn.app.base import BaseApplication

    class StandaloneApplication(BaseApplication):
        def __init__(self, app, options=None):
            self.options = options or {}
            self.application = app
            super(StandaloneApplication, self).__init__()

        def load_config(self):
            for key, value in self.options.items():
                if key in self.cfg.settings and value is not None:
                    self.cfg.set(key.lower(), value)

        def load(self):
            return self.application

    options = {
        'bind': '0.0.0.0:8000',
        'workers': 1,
    }
    StandaloneApplication(app, options).run()