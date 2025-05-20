import axios from "axios";
const API_URL = import.meta.env.VITE_API_URL;

export const getTransferencias = () => {
  axios.get(`${API_URL}/transferencias/`).then((res) => res.data);
};

export const createTransferencia = (data) =>
  axios.post(`${API_URL}/transferencias/`, data).then((res) => res.data);
