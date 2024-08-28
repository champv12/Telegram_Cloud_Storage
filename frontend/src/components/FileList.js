import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FileList() {
    const [files, setFiles] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchFiles = async () => {
            try {
                const response = await axios.get('/files');
                setFiles(response.data);
            } catch (error) {
                setError('Failed to fetch files');
                console.error(error);
            }
        };

        fetchFiles();
    }, []);

    return (
        <div>
            <h2>Your Files</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <ul>
                {files.map(file => (
                    <li key={file.id}>{file.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default FileList;
