import "./Admin.scss";
import React, {useEffect, useState} from 'react';
import Dashboard from "./Dashboard";
import LoginForm from "./LoginForm";


function Admin({connected_to_server, socket, connect, wifi}) {
    const [user, setUser] = useState({username: "", sid: ""})
    const [error, setError] = useState("");
    const [checking_credentials, setCheckingCredentials] = useState(false)


    useEffect(() => {
        connect();
    }, [])

    const showError=((msg)=>{
        setError(msg);
        setTimeout(() => {
            setError("");
        }, 2000);
    })

    const Login = details => {
        setCheckingCredentials(true);
        if (connected_to_server) {
            socket.emit("login", details, (response) => {
                if (response.result === "verified") {
                    setUser({username: details.username, sid: response.sid})
                } else {
                    showError(response.msg)
                }
                setCheckingCredentials(false)
            })
        } else {
            showError("Server Down, Try gain later")
            setCheckingCredentials(false)
        }
    }

    const Logout = () => {
        if (connected_to_server) {
            socket.emit("logout", user, (response) => {
                if (response.result !== "logged out") {
                    console.log(response);
                }
                setUser({username: "", sid: ""});
            })
        } else {
            setUser({username: "", sid: ""});
        }
    }

    return (
        <div className="main-admin-container">
            {(user.username !== "" && user.sid !== "") ?
                (<div><Dashboard connected_to_server={connected_to_server} wifi={wifi} socket={socket} user={user}
                                 Logout={Logout}/></div>) :
                (<div className={"login-container"}>
                    <LoginForm Login={Login} error={error} checking_credentials={checking_credentials} wifi={wifi}
                               connected_to_server={connected_to_server}/></div>)}
        </div>
    );
}

export default Admin;