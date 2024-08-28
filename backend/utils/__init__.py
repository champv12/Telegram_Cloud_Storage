from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
import os

# Import routes and handlers
from file_handler import handle_upload, handle_download
from config import Config

def create_app():
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app)
    
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # Define routes
    @app.route('/upload', methods=['POST'])
    def upload():
        try:
            if 'file' not in request.files:
                raise ValueError("No file part in the request")
            file = request.files['file']
            config = Config.from_env()
            responses = handle_upload(file, config.user_id, config.api_key, config.chat_id)
            return jsonify({"status": "success", "responses": responses})
        except Exception as e:
            logger.error(f"Error during file upload: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

    @app.route('/download', methods=['POST'])
    def download():
        try:
            file_id = request.form.get('file_id')
            config = Config.from_env()
            result = handle_download(file_id, config.user_id, config.api_key, config.chat_id)
            return jsonify(result)
        except Exception as e:
            logger.error(f"Error during file download: {e}")
            return jsonify({"status": "error", "message": str(e)}), 500

    return app

if __name__ == '__main__':
    app = create_app()
    debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() in ['true', '1', 't']
    app.run(debug=debug_mode)
