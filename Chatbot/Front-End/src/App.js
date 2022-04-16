import React, {useEffect, useState} from 'react';
import {BrowserRouter, Route, Routes} from "react-router-dom";
import {GoHome} from "react-icons/go";
import {BiWifi0, BiWifi2, BiWifiOff} from "react-icons/bi";
import Header from './Components/chat/Header';
import ChatLogin from './Components/chat/ChatLogin';
import Admin from "./Components/admin/Admin";
import io from "socket.io-client";
import "./App.scss";

function App() {
    const [socket, setSocket] = useState(undefined);
    const [connected_to_server, setConnectedToServer] = useState(false);
    const [wifi, setWifi] = useState(<BiWifi0/>)

    useEffect(() => { // janky code
        if (socket !== undefined) {
            socket.on('connect_error', function (err) {
                setWifi(<BiWifiOff className="failed-connection" style={{fill: "red"}}/>)
                setTimeout((() => {
                    setWifi(<BiWifiOff className="blink-icon" alt="Retry connection" onClick={connectToServer}/>)
                    socket.disconnect();
                    setSocket(undefined);
                    setConnectedToServer(false);
                }), 2000);
            })
            socket.on('connect', function () {
                setWifi(<BiWifi2/>)
                setConnectedToServer(true);
            })
        }
    }, [socket])


    function connectToServer() {
        setSocket(io.connect("http://localhost:3001"));
    }

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element=
                    {
                        <div className='MainPage'>
                            <Header wifi={wifi}/>
                            <ChatLogin connected_to_server={connected_to_server} socket={socket}
                                       connect={connectToServer}/>
                        </div>
                    }
                />
                <Route path="/admin"
                       element={<Admin connected_to_server={connected_to_server} socket={socket} wifi={wifi}
                                       connect={connectToServer}/>}/>
                <Route path="*" element={
                    <div style={{
                        display: "flex",
                        justifyContent: "center",
                        height: "100vh",
                        width: "100vw",
                        background: "rgb(255,255,255)"
                    }
                    }>
                        <div style={{
                            position: "relative"
                        }}>
                            < img style={{
                                height: "95vh"
                            }
                            } src={"404.jpg"} alt="Vectors by Vecteezy"/>
                            <a href={"/"}>
                                <GoHome style={
                                    {
                                        color: "black",
                                        height: "20vh",
                                        width: "20vw",
                                        position: "absolute",
                                        zIndex: "1",
                                        justifySelf: "center",
                                        top: "0",
                                        left: "0",
                                        right: "0",
                                        marginLeft: "auto",
                                        marginRight: "auto"
                                    }}/>
                            </a>
                            <a href="https://www.vecteezy.com/free-vector/404" target="_blank">
                                <text style={
                                    {
                                        position: "absolute",
                                        bottom: "20px",
                                        left: "0",
                                        right: "0",
                                        marginLeft: "auto",
                                        marginRight: "auto",
                                        color: "black"

                                    }}>
                                    Attribution to 404 Vectors by Vecteezy
                                </text>
                            </a>
                        </div>
                    </div>
                }/>
            </Routes>
        </BrowserRouter>
    );
}


export default App;
