import React from 'react';
import { render } from "react-dom";
import reportWebVitals from './reportWebVitals';
import MainPage from './MainPage';
import {
    BrowserRouter,
    Routes,
    Route,
} from "react-router-dom";
import Admin from "./Components/Admin";
const rootElement = document.getElementById('root');

render(
    <BrowserRouter>
        <Routes>
            <Route path="/" element={  <MainPage />} />
            <Route path="/N/A" element={
                <div>
                    Info not available
                </div>
            } />
            <Route path="/admin" element={<Admin />} />
            <Route path="*" element={
                <div>
                    <img src="404.jpg" alt={"404 Vectors by Vecteezy"}/>
                    <text>Attribution
                        <a href="https://www.vecteezy.com/free-vector/404">404 Vectors by Vecteezy</a>
                    </text>
                </div>
            } />
        </Routes>
    </BrowserRouter>,
    rootElement
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals(console.log);
