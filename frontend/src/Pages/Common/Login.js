import React, {Component} from "react";
import {Container, Row} from "react-bootstrap";
import {Link} from "react-router-dom";
import {Button, FormControlLabel, Checkbox, Paper, IconButton} from '@material-ui/core';
import CheckBoxOutlineBlankIcon from '@material-ui/icons/CheckBoxOutlineBlank';
import CheckBoxIcon from '@material-ui/icons/CheckBox';

import { connect } from "react-redux";
import { withRouter } from "react-router-dom";

import {loginAction} from "../../Redux/ActionCreators";
import { Formik, Form, Field } from 'formik';
import * as Yup from 'yup';

class Login extends Component{
    constructor(props) {
        super(props);
        this.state={
            user: this.props.session.user,
            remember: false,
            errorGlobal: '',
            visibility: false,
        };
    };

    
}