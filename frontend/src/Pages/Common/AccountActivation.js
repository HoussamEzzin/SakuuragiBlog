import React, {Component} from "react";
import {Container, Row} from "react-bootstrap";

class AccountActivation extends Component{
    constructor(props) {
        super(props);
        this.state={

        };
    };

    render(){
        return(
            <>
                <Row>
                    <div >
                        <Container>
                            <h1>
                                {this.props.message}
                                <h1>{this.props.email}</h1>,
                                Check your email (including spam)
                            </h1>
                        </Container>
                    </div>
                </Row>
            </>
        );
    }


}

export default AccountActivation;