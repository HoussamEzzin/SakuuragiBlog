import React, {Component} from "react";
import {BrowserRouter, Switch, Route, withRouter} from "react-router-dom";
import {connect} from 'react-redux';



class Main extends Component{
    constructor(props) {
        super(props);
        this.state={
            user: this.props.session.user
        }
    }
}