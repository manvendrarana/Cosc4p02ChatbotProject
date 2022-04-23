import "./Header.css";
import React, {useState} from 'react';
import {
    FaBars,
    FaBus,
    FaCode,
    FaDatabase,
    FaGlobe,
    FaHandsHelping,
    FaHashtag,
    FaMap,
    FaMedal,
    FaNewspaper,
    FaQuestion,
    FaRobot,
    FaServer,
    FaTicketAlt
} from 'react-icons/fa';
import element from "./Chat";


function Header({wifi}) {
    return (
        <Navbar>
            <NavItem icon={<FaBars/>}>{
                <DropdownMenu/>
            }
            </NavItem>
            <title>Niagara 2022 Games ChatBot</title>
            <NavItem icon={<FaHandsHelping/>}>{
                <DevsDropdownMenu/>
            }
            </NavItem>
            <NavItem icon={<FaMap/>}>{
                <TransitDropdownMenu/>
            }
            </NavItem>
            <NavItem icon={wifi}/>
        </Navbar>
    );
}

function TransitDropdownMenu() {
    return (
        <div className="transit-dropdown">
            <a href="https://www.niagararegion.ca/transit/" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-right"></span>
                <h4 className="label">Niagara Transit</h4>
                <span className="icon-button"><FaBus/></span>
            </a>
            <a href="https://www.niagararegion.ca/transit/routes.aspx?home_task=1" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-right"></span>
                <h4 className="label">St. Catharines Transit</h4>
                <span className="icon-button"><FaBus/></span>
            </a>

        </div>
    );
}

function DevsDropdownMenu() {
    element.innerHTML = "Waiting for user...";
    return (
        <div className="devs-dropdown">
            <h1 className="devs-Heading">Support Team</h1>
            <a className="devs-item" href="https://github.com/CaptKillSwitch" target="_blank" rel="noreferrer">
                Rikveet Singh Hayer - AI, Scraping<br></br>rh18vo@gmail.com
                <span className="devs-icon-button"><FaRobot/></span>
            </a>
            <a className="devs-item" href="https://github.com/SagerKudrick" target="_blank" rel="noreferrer">
                Sager Kudrick - Back-End<br></br>sagerkudrick@hotmail.com
                <span className="devs-icon-button"><FaServer/></span>
            </a>
            <a className="devs-item" href="https://github.com/sawyerfenwick" target="_blank" rel="noreferrer">
                Sawyer Fenwick - Back-End<br></br>sawyerfenwick@gmail.com
                <span className="devs-icon-button"><FaServer/></span>
            </a>
            <a className="devs-item" href="https://github.com/mraman3" target="_blank" rel="noreferrer">
                Aman Braich - Front-End<br></br>braich_aman3@yahoo.ca
                <span className="devs-icon-button"><FaCode/></span>
            </a>
            <a className="devs-item">
                Raghav Bhardwaj - Front-End<br></br>raghavmanc@gmail.com
                <span className="devs-icon-button"><FaCode/></span>
            </a>
            <a className="devs-item" href="https://github.com/d3v3lopingCod3" target="_blank" rel="noreferrer">
                Manvendrasinh Rana - Scraping<br></br>manvendrarana@hotmail.com
                <span className="devs-icon-button"><FaDatabase/></span>
            </a>
            <a className="devs-item" href="https://github.com/EddySu718" target="_blank" rel="noreferrer">
                Eddy Su - Scraping<br></br>eddysu123@gmail.com
                <span className="devs-icon-button"><FaDatabase/></span>
            </a>
            <h3 className="devs-text">Support team will reach out to you within</h3>
            <h3 className="devs-text">3-5 business days</h3>
        </div>
    );
}

function DropdownMenu() {
    return (
        <div className="dropdown">
            <a href="https://niagara2022games.ca/" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-button"><FaGlobe/></span>
                <ul>
                    <h4 className="label">Niagara Games 2022<br></br></h4>
                    <text className="label">Visit Niagara 2022 Games website</text>
                </ul>
                <span className="icon-right"></span>
            </a>
            <a href="https://niagara2022games.ca/tickets/" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-button"><FaTicketAlt/></span>
                <ul>
                    <h4 className="label">Tickets<br></br></h4>
                    <text className="label">Purchase tickest for Niagara 2022 Games</text>
                </ul>
                <span className="icon-right"></span>
            </a>
            <a href="https://niagara2022games.ca/news/" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-button"><FaNewspaper/></span>
                <ul>
                    <h4>News<br></br></h4>
                    <text className="label">Latest news on Niagara 2022 Games</text>
                </ul>
                <span className="icon-right"></span>
            </a>
            <a href="https://niagara2022games.ca/media/releases/" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-button"><FaHashtag/></span>
                <ul>
                    <h4>Media Releases<br></br></h4>
                    <text className="label">Latest headlines from games host society</text>
                </ul>
                <span className="icon-right"></span>
            </a>
            <a href="https://niagara2022games.ca/about/alumni/" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-button"><FaMedal/></span>
                <ul>
                    <h4>Canada Games Alumni<br></br></h4>
                    <text className="label">Learn about alumni athletes and coaches</text>
                </ul>
                <span className="icon-right"></span>
            </a>
            <a href="https://www.niagarathisweek.com/niagarafalls-on-news/" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-button"><FaNewspaper/></span>
                <ul>
                    <h4>Local News<br></br></h4>
                    <text className="label">Latest news of events in Niagara Falls</text>
                </ul>
                <span className="icon-right"></span>
            </a>
            <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ" className="menu-item" target="_blank"
               rel="noreferrer">
                <span className="icon-button"><FaQuestion/></span>
                <ul>
                    <h4>Help<br></br></h4>
                    <text className="label">Watch tutorial video on chatbot</text>
                </ul>
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
