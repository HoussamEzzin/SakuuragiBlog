import React from "react";
import {Link} from "react-router-dom";
const Header = () =>{
    return(
        <nav className="navbar navbar-expand navbar-dark bg-dark d-flex justify-content-between">
            <a href="/" className="navbar-brand">

                SakuuragiBlog
            </a>
            <div className="navbar-nav mr-auto">
                <li className="nav-item">
                    <Link to="/register" className="nav-link">
                        Register
                    </Link>
                </li>
                <li className="nav-item">
                    <Link to="/login" className="nav-link">
                        Login
                    </Link>
                </li>
            </div>


        </nav>
    );
}

export default  Header;