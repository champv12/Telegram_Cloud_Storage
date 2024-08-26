import axios from 'axios';

const api = axios.create({
    baseURL: 'http://localhost:5000',  // Replace with your backend URL
});

export const uploadFile = (formData) => {
    return api.post('/upload', formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
};

export const downloadFile = (fileId, userId, apiKey, chatId) => {
    return api.get('/download', {
        params: { file_id: fileId, user_id: userId, api_key: apiKey, chat_id: chatId },
        responseType: 'blob'
    });
};