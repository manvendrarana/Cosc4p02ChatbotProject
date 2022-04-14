import "./Dashboard.scss";
import React from 'react';


function Dashboard({wifi, user, Logout}) {

    return (
        <div className="main-dashboard-container">
            <div className="navbar">
                {wifi}
                <button className="navbar-button">
                    Component Status
                </button>
                <button className="navbar-button">
                    Tests
                </button>
                <button className="navbar-button">
                    Data
                </button>
            </div>
            <div className="dashboard-container">
                <div className="dashboard-content">

                </div>
            </div>
        </div>
    );
}

export default Dashboard;