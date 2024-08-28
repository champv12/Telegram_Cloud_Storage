import React, { useState } from 'react';
import axios from 'axios';

function FileUploader() {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        if (!file) {
            setMessage('Please select a file to upload.');
            return;
        }

        const formData = new FormData();
        formData.append('file', file);
        formData.append('user_id', process.env.REACT_APP_USER_ID);  // Use environment variables
        formData.append('api_key', process.env.REACT_APP_API_KEY);  // Use environment variables
        formData.append('chat_id', process.env.REACT_APP_CHAT_ID);  // Use environment variables

        setLoading(true);
        setMessage('');

        try {
            const response = await axios.post('/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            setMessage('File uploaded successfully!');
            console.log(response.data);
        } catch (error) {
            setMessage('Failed to upload file.');
            console.error(error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload} disabled={loading}>
                {loading ? 'Uploading...' : 'Upload'}
            </button>
            {message && <p>{message}</p>}
        </div>
    );
}

export default FileUploader;
