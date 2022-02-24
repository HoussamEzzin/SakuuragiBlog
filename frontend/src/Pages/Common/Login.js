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

    handleRemeber =( ) => {
        this.setState({
            remember: !this.state.remember
        })
    }

    handleVisibility = () => {
        this.setState({
            visibility: !this.state.visibility
        })
    }

    componentDidMount() {
        const user = this.props.session.user;
        if(user){
            if(user.is_reader){
                return this.props.history.push("/reader");
            }else{
                return this.props.history.push("/publisher");
            }
        }
    }

    handleSubmit = (values) => {
        const data = {
            "email": values.email,
            "password": values.password,
        };
        return this.props
            .dispatch(loginAction(data))
            .then(data => {
                if(data.payload.Success){
                    setTimeout(()=>{
                        if(data.payload.user.is_reader){
                            this.props.history.push("/reader/dashboard");
                        }
                        if(data.payload.user.is_publisher){
                            this.props.history.push("/publisher/dashboard");
                        }
                    }, 3000);
                }
            })
            .catch(err=> {
                console.log("err", err);
                this.setState({
                    errorGlobal: err.message
                });
            });
    };

    render() {
        const {errorGlobal} = this.state;
        return(
            <>
                <Row>
                    <div>
                        <Container>
                            <h1>Log In</h1>
                        </Container>
                        {errorGlobal && (
                            <div>Error</div>
                        )}
                        <Container>
                            <Formik
                                initialValues={{ email:'', password:''}}
                                validationSchema={Yup.object({
                                    password: Yup.string()
                                        .min(6,'Must be 6 characters or more')
                                        .required('Required'),
                                    email: Yup.string()
                                        .email('Invalid email address')
                                        .required('Required'),
                                })}
                                onSubmit={(values, {setSubmitting})=> {
                                    setTimeout(()=>{
                                        this.handleSubmit(values)
                                        setSubmitting(false);
                                    }, 400);
                                }}>
                            {/*    UNCOMPLETE*/}
                            </Formik>
                        </Container>
                    </div>
                </Row>
            </>
        )
    }
}