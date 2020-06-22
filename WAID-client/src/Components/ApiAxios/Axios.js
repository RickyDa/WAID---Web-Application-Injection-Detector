import axios from 'axios';
import https from 'https';

const dataAddress = process.env.REACT_APP_ARG


export const userAxios =  axios.create({
    baseURL: `https://${dataAddress}:5000/user`,
    headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Authorization'
    }
});

export const ruleAxios = axios.create({
    baseURL: `https://${dataAddress}:5000/rule`,
    headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Authorization'
    },
    httpsAgent: new https.Agent({
        rejectUnauthorized: false
    }),
});

export const confAxios = axios.create({
    baseURL: `https://${dataAddress}:5000/conf`,
    headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Authorization'},
    httpsAgent: new https.Agent({
        rejectUnauthorized: false,
    })
});

export const demoAxios = axios.create({
    baseURL: `https://${dataAddress}:5000`,
    headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
        'Access-Control-Allow-Headers': 'Authorization'}
});

