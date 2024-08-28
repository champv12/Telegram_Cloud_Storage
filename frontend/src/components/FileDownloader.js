import React, { useState } from 'react';
import axios from 'axios';

function FileDownloader() {
    const [fileId, setFileId] = useState('');
    const [error, setError] = useState(null);

    const handleDownload = async () => {
        try {
            const response = await axios.get('/download', {
                params: {
                    file_id: fileId,
                    user_id: 'user_id',  // Replace with actual user_id
                    api_key: 'api_key',  // Replace with actual api_key
                    chat_id: 'chat_id'   // Replace with actual chat_id
                },
                responseType: 'blob'
            });
            const url = window.URL.createObjectURL(new Blob([response.data]));
            const link = document.createElement('a');
            link.href = url;
            link.setAttribute('download', 'file.mp4');  // Replace with actual file name
            document.body.appendChild(link);
            link.click();
            link.remove();
        } catch (error) {
            setError('Failed to download file');
            console.error(error);
        }
    };

    return (
        <div>
            <input
                type="text"
                value={fileId}
                onChange={(e) => setFileId(e.target.value)}
                placeholder="Enter file ID"
            />
            <button onClick={handleDownload}>Download</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
        </div>
    );
}

export default FileDownloader;
