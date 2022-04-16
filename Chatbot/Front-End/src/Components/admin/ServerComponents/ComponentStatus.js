import React, {useEffect, useState} from 'react';
import {IoReloadCircleSharp} from "react-icons/io5";
import {FaWindowClose} from "react-icons/fa";
import {RiNotificationBadgeFill, RiNotificationBadgeLine} from "react-icons/ri";
import "./ComponentStatus.scss";

function Component({type, status_components, setShowMsg, setMsg}) {
    let status = status_components[type]["status"];
    let msg_log = status_components[type]["msg_log"];
    const [current_status_class_name, setCurrentStatusClassName] = useState("status-not-connected")

    const [notification_icon, setNotificationIcon] = useState(<RiNotificationBadgeLine className="notification-icon"/>)

    useEffect(() => {
        setNotificationIcon(<RiNotificationBadgeFill className="notification-icon" onClick={() => {
            setNotificationIcon(<RiNotificationBadgeLine onClick={() => {
                setMsg(msg_log);
                setShowMsg(true);
            }} className="notification-icon"/>)
            setMsg(msg_log);
            setShowMsg(true)
        }}/>)
    }, [status_components])

    useEffect(() => {
        switch (status) {
            case "not_initialized":
                setCurrentStatusClassName("status-not-initialized");
                break;
            case "working":
                setCurrentStatusClassName("status-working");
                break;
            case "busy":
                setCurrentStatusClassName("status-busy");
                break;
            case "error":
                setCurrentStatusClassName("status-error");
                break;
            default:
                setCurrentStatusClassName("status-not-connected");
        }
    }, [status])

    return (
        <div className={"component " + current_status_class_name}>
            {notification_icon}
            <div className="type">{type}</div>
            <div className="status">{status}</div>
        </div>)
}

function ComponentStatus({connected_to_server, sid, socket}) {
    const [status_components, setStatusComponents] = useState({
        "scraper": {
            "status": "not_initialized",
            "msg_log": []
        },
        "database": {
            "status": "not_initialized",
            "msg_log": []
        },
        "ai": {
            "status": "not_initialized",
            "msg_log": []
        },
        "test": {
            "status": "not_initialized",
            "msg_log": []
        }
    })

    const [num_connected_users, setNumConnectedUsers] = useState(0);

    const [error, setError] = useState("");

    const [seconds_passed, setSecondsPassed] = useState(0)

    const [showMsg, setShowMsg] = useState(false)

    const [msg, setMsg] = useState([])

    useEffect(() => {
        if (connected_to_server) {
            socket.on("update_components", (details) => {
                setSecondsPassed(0);
                setNumConnectedUsers(details["num_users_connected"]);
                let tempDetails = status_components
                for (const [type, values] of Object.entries(status_components)) {
                    tempDetails[type]["status"] = details["components_status"][type]["status"]
                    tempDetails[type]["msg_log"].unshift(...details["components_status"][type]["msg_log"])
                }
                setStatusComponents(tempDetails);
            })
        } else {
            setError("Server Down")
        }
    }, [connected_to_server])

    useEffect(() => {
        let counterInterval = setInterval(() => setSecondsPassed(seconds_passed + 1), 1000);
        return () => {
            clearInterval(counterInterval);
        }
    }, [seconds_passed])

    useEffect(() => {
        socket.emit("components_update_request", sid, (response) => {
            if (response["result"] === "failed") {
                setError(response["msg"]);
            } else {
                setError("");
            }
        })
    }, [])

    function getTime() {
        let total_seconds = seconds_passed;
        let hours = Math.floor(seconds_passed / (60 * 60))
        total_seconds -= (hours * (60 * 60));
        let minutes = Math.floor(total_seconds / 60)
        total_seconds -= (minutes * 60);
        hours = (hours).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping: false})
        minutes = (minutes).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping: false})
        total_seconds = (total_seconds).toLocaleString('en-US', {minimumIntegerDigits: 2, useGrouping: false})
        return hours + ":" + minutes + ":" + total_seconds;
    }

    return (
        <div className="component-status-container">
            <div className="component-status-header">
                <div className="users_connected">Number of users connected {num_connected_users}</div>
                <div className="seconds">Time since last update {getTime()}s</div>
            </div>
            <IoReloadCircleSharp aria-readonly={!connected_to_server}
                                 style={!connected_to_server ? {cursor: "not-allowed"} : {}}
                                 onClick={() => {
                                     socket.emit("components_update_request", sid, (response) => {
                                         if (response["result"] === "failed") {
                                             setError(response["msg"]);
                                         } else {
                                             setError("");
                                         }
                                     })
                                 }}/>
            <div className="components">
                <div className={showMsg ? "msg-log-container show" : "msg-log-container"}>
                    <h1>Log History</h1>
                    <FaWindowClose style={{cursor:"pointer"}} onClick={() => {
                        setShowMsg(false)
                    }}/>
                    <div className="msg">
                        {
                            msg.map((m) => {
                                return (
                                    <li>{m}</li>
                                )
                            })
                        }
                    </div>
                </div>
                <Component type={"scraper"} status_components={status_components} setMsg={setMsg}
                           setShowMsg={setShowMsg}/>
                <Component type={"database"} status_components={status_components} setMsg={setMsg}
                           setShowMsg={setShowMsg}/>
                <Component type={"ai"} status_components={status_components} setMsg={setMsg} setShowMsg={setShowMsg}/>
                <Component type={"test"} status_components={status_components} setMsg={setMsg} setShowMsg={setShowMsg}/>
            </div>
            <div className="component-status-footer">
                <div className="error">{error}</div>
            </div>

        </div>)
}

export default ComponentStatus;