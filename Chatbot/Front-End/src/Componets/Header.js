import "./Header.css";
import React from 'react';
import { FaCog } from 'react-icons/fa';
import { FaBars } from 'react-icons/fa';
import { FaTicketAlt } from 'react-icons/fa';
import { FaGlobe } from 'react-icons/fa';
import { useState } from 'react';


function Header() {
    return (
        <Navbar>
            <NavItem icon={<FaBars />}>{
                <DropdownMenu />
            }</NavItem>
            <li className="nav-item">
                <a href='settings' className="icon-button">
                    <FaCog />
                </a>
            </li>
            <title>CHAT BOT NAME HERE</title>
        </Navbar>
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
