from flask import Flask, request, jsonify
from file_handler import handle_upload, handle_download
from telegram_api import setup_telegram

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    user_id = request.form['user_id']
    api_key = request.form['api_key']
    chat_id = request.form['chat_id']
    response = handle_upload(file, user_id, api_key, chat_id)
    return jsonify(response)

@app.route('/download', methods=['GET'])
def download_file():
    file_id = request.args.get('file_id')
    user_id = request.args.get('user_id')
    api_key = request.args.get('api_key')
    chat_id = request.args.get('chat_id')
    response = handle_download(file_id, user_id, api_key, chat_id)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)