import "./Admin.scss";
import React, {useEffect, useState} from 'react';
import Dashboard from "./Dashboard";
import LoginForm from "./LoginForm";


function Admin({socket, connect, wifi}) {
    const [user, setUser] = useState({username: "user", sid: "sid"})
    const [error, setError] = useState("");
    const [checking_credentials, setCheckingCredentials] = useState(false)

    useEffect(() => {
        connect();
    }, [])

    const Login = details => {
        setCheckingCredentials(true);
        if (socket !== undefined && socket.connected) {
            socket.emit("login", details, (response) => {
                if (response.result === "verified") {
                    setUser({username: details.username, sid: response.sid})
                    console.log(response)
                } else {
                    setError(response.msg);
                }
                setCheckingCredentials(false)
            })
        } else {
            setError("Server Down, Try gain later")
            setCheckingCredentials(false)
        }
    }

    const Logout = () => {
        socket.emit("logout", user, (response) => {
            if (response.result !== "logged out") {
                console.log(response);
            }
            setUser({username: "", sid: ""});
        })
    }

    return (
        <div className="main-admin-container">
            {(user.username !== "" && user.sid !== "") ?
                (<div><Dashboard wifi={wifi} user={user} Logout={Logout}/></div>) :
                (<div className={"login-container"}>
                <LoginForm Login={Login} error={error} checking_credentials={checking_credentials}/></div>)}
        </div>
    );
}

export default Admin;