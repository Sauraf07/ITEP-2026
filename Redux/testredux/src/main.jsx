import React from 'react'
import ReactDom from 'react-dom/client'
import App from './App.jsx'
import {Provider } from "react-redux";
import store from "./redux-config/MyStore.js";

const {createRoot} = ReactDom;

createRoot(document.getElementById('root')).render(

  <Provider store= {store}>
    <App />
  </Provider>
);