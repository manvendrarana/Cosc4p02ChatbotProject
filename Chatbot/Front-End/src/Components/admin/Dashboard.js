import "./Dashboard.scss";
import React, {useEffect, useState} from 'react';
import {RiMenuUnfoldLine} from "react-icons/ri";
import ComponentStatus from "./ServerComponents/ComponentStatus";
import DataVisualizer from "./ServerComponents/DataVisualizer";
import TestResults from "./ServerComponents/TestResults";

function Dashboard({connected_to_server, wifi, socket, user, Logout}) {
    const [show_menu, setShowMenu] = useState(false);
    const [dashboard_tab, setDashboardType] = useState("component_status");

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
                <div className="dashboard-content">
                    {
                        {
                            "component_status": <ComponentStatus connected_to_server={connected_to_server}
                                                                 sid={user.sid} socket={socket}/>,
                            "show_data": <DataVisualizer connected_to_server={connected_to_server} sid={user.sid}
                                                         socket={socket}/>,
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