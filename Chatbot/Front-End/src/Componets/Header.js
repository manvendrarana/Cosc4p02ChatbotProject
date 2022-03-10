import "./Header.css";
import React from 'react';
import { FaCog } from 'react-icons/fa';
import { FaBars } from 'react-icons/fa';
import { FaTicketAlt } from 'react-icons/fa';
import { FaGlobe } from 'react-icons/fa';
import { FaQuestion } from 'react-icons/fa';
import { FaHandsHelping } from 'react-icons/fa';
import { FaRobot } from 'react-icons/fa';
import { FaCode } from "react-icons/fa";
import { FaServer } from "react-icons/fa";
import { FaDatabase } from "react-icons/fa";

import { useState } from 'react';

function Header() {
    return (
        <Navbar>
            <NavItem icon={<FaBars />}>{
                <DropdownMenu />
            }
            </NavItem>
            <li className="nav-item">
                <a href='ssettings' className="icon-button">
                    <FaCog />
                </a>
            </li>
            
            <title>CHAT BOT NAME HERE</title>
            <NavItem icon={<FaHandsHelping />}>{
                <DevsDropdownMenu />
            }
            </NavItem>
        </Navbar>
    );
}


function DevsDropdownMenu() {
    return (
        <div className="devs-dropdown">
            <h1 className="devs-Heading">Support Team</h1>
            <a  className="devs-item">
                Rikveet Singh Hayer - AI, Scraping<br></br>rh18vo@gmail.com
                <span className="devs-icon-button"><FaRobot /></span>
            </a>
            <a  className="devs-item">
                Sager Kudrick - Back-End<br></br>sagerkudrick@hotmail.com
                <span className="devs-icon-button"><FaServer /></span>
            </a>
            <a  className="devs-item">
                Sawyer Fenwick - Back-End<br></br>sawyerfenwick@gmail.com
                <span className="devs-icon-button"><FaServer /></span>
            </a>
            <a  className="devs-item">
                Aman Braich - Front-End<br></br>braich_aman3@yahoo.ca
                <span className="devs-icon-button"><FaCode /></span>
            </a>
            <a  className="devs-item">
                Raghav Bhardwaj - Front-End<br></br>raghavmanc@gmail.com
                <span className="devs-icon-button"><FaCode /></span>
            </a>
            <a  className="devs-item">
                Manvendrasinh Rana - Scraping<br></br>manvendrarana@hotmail.com
                <span className="devs-icon-button"><FaDatabase /></span>
            </a>
            <a  className="devs-item">
                Eddy Su - Scraping<br></br>eddysu123@gmail.com
                <span className="devs-icon-button"><FaDatabase /></span>
            </a>
            <h3 className="devs-text">Support team will reach out to you within</h3>
            <h3 className="devs-text">3-5 business days</h3>
        </div>
    );
}

function DropdownMenu() {
    return (
        <div className="dropdown">
            <a href="https://niagara2022games.ca/" className="menu-item">
                <span className="icon-button"><FaGlobe /></span>
                Visit Niagara Games 2022
                <span className="icon-right"></span>
            </a>
            <a href="https://niagara2022games.ca/tickets/" className="menu-item">
                <span className="icon-button"><FaTicketAlt /></span>
                Buy Tickets Here
                <span className="icon-right"></span>
            </a>
            <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" className="menu-item">
                <span className="icon-button"><FaQuestion /></span>
                    Help
                <span className="icon-right"></span>
            </a>
        </div>
    );
}

function Navbar(props) {
    return (
        <nav className="navbar">
            <ul className="navbar-nav">{props.children}</ul>
        </nav>
    );
}

function NavItem(props) {
    const [open, setOpen] = useState(false);
    return (
        <li className="nav-item">
            <a className="icon-button" onClick={() => setOpen(!open)}>
                {props.icon}
            </a>
            {open && props.children}
        </li>
    );
}
export default Header;
