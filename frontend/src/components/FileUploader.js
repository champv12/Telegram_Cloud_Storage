import React, { useState } from 'react';
import axios from 'axios';

function FileUploader() {
    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    };

    const handleUpload = async () => {
        const formData = new FormData();
        formData.append('file', file);
        formData.append('user_id', 'user_id');  // Replace with actual user_id
        formData.append('api_key', 'api_key');  // Replace with actual api_key
        formData.append('chat_id', 'chat_id');  // Replace with actual chat_id

        try {
            const response = await axios.post('/upload', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log(response.data);
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <div>
            <input type="file" onChange={handleFileChange} />
            <button onClick={handleUpload}>Upload</button>
        </div>
    );
}

export default FileUploader;