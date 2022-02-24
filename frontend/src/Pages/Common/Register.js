import React, {Component} from "react";
import {Container, Row, CardColumns} from "react-bootstrap";
import {Link} from "react-router-dom";

class Register extends Component{
    constructor(props) {
        super(props);
        this.state = {

        };
    };

    render(){
        return(
            <>
                <div className="container mt-5 align-content-center text-center">
                    <div className="d-flex flex-column align-content-center align-items-center">
                        <Container className="modal-title">
                            <h1 className="title"> Create an Account </h1>
                        </Container>
                        <Row >
                            <Link className="btn btn-primary m-5"
                                    to="/register/reader"
                            >
                                Reader
                            </Link>
                            <Link className="btn btn-primary m-5"
                                  to="/register/publisher"
                            >
                                Apply for publishing
                            </Link>
                        </Row>
                        <Container>
                            <span>Already have an account ?
                            <Link to="/login">
                                Login
                            </Link>
                            </span>
                        </Container>

                    </div>

                </div>
            </>
        )
    }
}

export default Register;