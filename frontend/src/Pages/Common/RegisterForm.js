import React , {Component} from "react";
import {Container, Row} from "react-bootstrap";
import {Link} from "react-router-dom";
import {Button, IconButton, Paper} from "@material-ui/core";

import {Formik, Form, Field} from 'formik';
import * as Yup from 'yup';

import {connect} from "react-redux";
import {withRouter} from "react-router-dom";

import AccountActivation from "./AccountActivation";

import {publisher_registerAction, readerRegisterAction} from "../../Redux/ActionCreators";


class RegisterForm extends Component{
    constructor(props) {
        super(props);
        this.state = {
            errorGlobal: "",
            registerSuccess: false,
            registerMessgae: false,
            is_reader: this.props.match.params.user === "reader",
            is_publisher : this.props.match.params.user === "publisher",
            email:"",
            description: "",
        };
    };

    handleDescription = ({target}) => {
        this.setState({
            description: target.value
        })
    }

    handleSubmit = (values) => {
        let formData = new FormData();
        formData.append("email", values.email);
        formData.append("username", values.username);
        formData.append("password", values.password);
        formData.append("is_reader", this.state.is_reader);
        formData.append("is_publisher", this.state.is_publisher);

        if(this.state.is_reader){
            return this.props.dispatch(readerRegisterAction(formData))
                .then(data => {
                    if(data.payload.Success){
                        // TODO: add google analytics
                        this.setState({
                            registerSuccess: true,
                            email: values.email,
                            registerMessage: "Activate your account"
                        })
                    }
                })
                .catch(err=>{
                    console.log("err",err);
                    this.setState({
                        errGlobal: err.message
                    });
                });
        }
        if(this.state.is_publisher){
            return this.props.dispatch(publisher_registerAction(formData))
                .then(data => {
                    if(data.payload.Success){
                        this.setState({
                            registerSuccess:true,
                            email: values.email,
                            registerMessage:"Activate your account"
                        })
                    }
                })
                .catch(err=> {
                    console.log("err",err);
                    this.setState({
                        errorGlobal: err.message
                    });
                });
        }

    }

    render(){
        const {errorGlobal, description, registerMessage} = this.state;
        return(
            <>
                {this.state.registerSuccess === false ?
                    <div className="container mt-5 align-content-center text-center">
                        <div className="d-flex flex-column align-content-center align-items-center">
                            <Container className="modal-title">
                                <h1 className="title"> Register </h1>
                            </Container>
                            {errorGlobal && (
                                <div className="text-center">{errorGlobal}</div>
                            )}
                            <Container>
                                <Formik
                                initialValues={ {email:'',password:'',username:''}}
                                validationSchema={Yup.object({
                                    password: Yup.string()
                                        .min(6, "Must be 6 characters or more")
                                        .required('Required'),
                                    username: Yup.string()
                                        .min(4, 'Must be 4 characters or more')
                                        .required('Required'),
                                    email: Yup.string().email('Invalid email address')
                                        .required('Required')
                                })}
                                onSubmit={(values, {setSubmitting}) => {
                                    setTimeout(() => {
                                        this.handleSubmit(values)
                                        setSubmitting(false);
                                    }, 400);
                                }}
                                >
                                    {({
                                        isSubmitting,
                                        values,
                                        errors,
                                        touched,
                                        isValidating,
                                        setFieldValue
                                    }) => (
                                        <Form>
                                            <span>Email</span>
                                            <Paper>
                                                <Field
                                                    name="email"
                                                    value={values.email}
                                                />
                                            </Paper>
                                            <div>
                                                {errors.email && touched.email}
                                            </div>
                                            <span>Username</span>
                                            <Paper>
                                                <Field
                                                    type="text"
                                                    name="username"
                                                    value={values.username}
                                                />
                                            </Paper>
                                            <div>
                                                {errors.username && touched.username}
                                            </div>
                                            <span>Password</span>
                                            {/*TODO: ADD PASSWORD VISIBILITY*/}
                                            <Paper>
                                                <Field
                                                    type="password"
                                                    name="password"
                                                    value={values.password}
                                                />

                                            </Paper>
                                            <div>
                                                {errors.password && touched.password}
                                            </div>
                                            {this.props.match.params.user === "publisher" ?
                                            <>
                                                <span>Description</span>
                                                <Paper>
                                                    <input type="text"
                                                            name="description"
                                                           value={description}
                                                           onChange={this.handleDescription}
                                                    />
                                                </Paper>

                                            </>
                                                :null
                                            }
                                            <Button
                                                type="submit"
                                                variant="contained"
                                                color="secondary"
                                            >
                                                Submit
                                            </Button>
                                        </Form>
                                    )}
                                </Formik>
                            </Container>
                            <Container >
                                <span>Already have an account ?</span><Link to="/login"> Login</Link>
                            </Container>

                        </div>

                    </div>
                    :
                    <AccountActivation
                        email={this.state.email}
                        message={registerMessage}
                    />
                }
            </>
        );
    }
}

const mapStateToProps = state => ({session: state.session});
export default connect(mapStateToProps)(withRouter(RegisterForm));