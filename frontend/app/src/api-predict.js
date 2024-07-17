import axios from 'axios';

const api_predict = axios.create({
    baseURL: 'http://localhost:8001'
});

export default api_predict;

