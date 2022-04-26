import "./Dashboard.scss";
import React, {useEffect, useState} from 'react';
import {RiMenuUnfoldLine} from "react-icons/ri";
import ComponentStatus from "./ServerComponents/ComponentStatus";
import DataVisualizer from "./ServerComponents/DataVisualizer";
import TestResults from "./ServerComponents/TestResults";

function Dashboard({connected_to_server, wifi, socket, user, Logout}) {
    const [show_menu, setShowMenu] = useState(false);
    const [dashboard_tab, setDashboardType] = useState("component_status");
    const [showErr, setShowErr] = useState(false);
    const [error, setError] = useState("");
    const [status_components, setStatusComponents] = useState({
        "scraper": {
            "status": "not_initialized", "msg_log": []
        }, "database": {
            "status": "not_initialized", "msg_log": []
        }, "ai": {
            "status": "not_initialized", "msg_log": []
        }, "test": {
            "status": "not_initialized", "msg_log": []
        }
    })
    const [data, setData] = useState([{
        "url":"n/a",
        "title": "Sample Title",
        "section_title": "Sample Section",
        "columns": ["heading1","heading2","heading3"],
        "values": [["x","y","z"],["x","y","z"],["x","y","z"],["x","y","z"]]
    }])
    useEffect(()=>{
        if(!connected_to_server){
            Logout();
        }
    },[connected_to_server])

    useEffect(()=>{
        if(connected_to_server){
            socket.emit("check_sid",user.sid,(response)=>{
                if(response["result"]!=="verified"){
                    Logout();
                }
            })
        }
    },[])//verify still logged in

    function showError(error_msg){
        setError(error_msg);
        setShowErr(true);
    }

    return (
        <div className="main-dashboard-container">
            <div className="hamburger" style={show_menu ? {display: "none"} : {}} onClick={() => {
                setShowMenu(true)
            }}>
                <RiMenuUnfoldLine/>
            </div>
            <div className="navbar" style={show_menu ? {display: "flex"} : {}}>
                <div className="user">{user.username}</div>
                <button onClick={() => {
                    setShowMenu(false);
                    setDashboardType("component_status");
                }} className={dashboard_tab === "component_status" ? "navbar-button active" : "navbar-button"}>
                    Component Status
                </button>
                <button onClick={() => {
                    setShowMenu(false);
                    setDashboardType("test");
                }} className={dashboard_tab === "test" ? "navbar-button active" : "navbar-button"}>
                    Tests
                </button>
                <button onClick={() => {
                    setShowMenu(false);
                    setDashboardType("show_data");
                }} className={dashboard_tab === "show_data" ? "navbar-button active" : "navbar-button"}>
                    Scraped Data
                </button>
                <button onClick={() => {
                    setShowMenu(false);
                    Logout();
                }} className="navbar-button">
                    Logout
                </button>
                {wifi}
            </div>

            <div className="dashboard-container">
                <div className="error" style={showErr ? {display: "flex"}: {display: "none"}}>
                    <text>{ error}</text>
                    <button onClick={()=>{
                        console.log(showErr)
                        setError("");
                        setShowErr(false);
                    }}>Ok</button>
                </div>
                <div className="dashboard-content">
                    {
                        {
                            "component_status": <ComponentStatus connected_to_server={connected_to_server} sid={user.sid}
                                                                 socket={socket} showError={showError}
                                                                 status_components={status_components}
                                                                 setStatusComponents={setStatusComponents}/>,
                            "show_data": <DataVisualizer connected_to_server={connected_to_server} sid={user.sid}
                                                         socket={socket} showError={showError} data={data} setData={setData}/>,
                            "test": <TestResults connected_to_server={connected_to_server} sid={user.sid}
                                                 socket={socket}/>
                        }[dashboard_tab]
                    }
                </div>
            </div>
        </div>
    );
}

export default Dashboard;