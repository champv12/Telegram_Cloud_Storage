import React, { useState, useEffect } from 'react';
import axios from 'axios';

function FileList() {
    const [files, setFiles] = useState([]);

    useEffect(() => {
        // Fetch files from backend
        const fetchFiles = async () => {
            try {
                const response = await axios.get('/files');
                setFiles(response.data);
            } catch (error) {
                console.error(error);
            }
        };

        fetchFiles();
    }, []);

    return (
        <div>
            <h2>Your Files</h2>
            <ul>
                {files.map(file => (
                    <li key={file.id}>{file.name}</li>
                ))}
            </ul>
        </div>
    );
}

export default FileList;