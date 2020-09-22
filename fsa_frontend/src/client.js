import Axios from 'axios';
import queryString from 'query-string';

const client = Axios.create({
  baseURL: process.env.API_URL,
  paramsSerializer: params => queryString.stringify(params, { arrayFormat: 'index' }),
  headers: {
    'Content-Type': 'application/json',
  }
});

export default client;
