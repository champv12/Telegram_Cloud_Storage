import React from 'react';
import FileUploader from './components/FileUploader';
import FileList from './components/FileList';
import FileDownloader from './components/FileDownloader';

function App() {
    return (
        <div>
            <h1>Teledrive</h1>
            <FileUploader />
            <FileList />
            <FileDownloader />
        </div>
    );
}

export default App;