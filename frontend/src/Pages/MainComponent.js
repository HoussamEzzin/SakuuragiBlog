import React, {Component} from "react";
import {BrowserRouter, Switch, Route, withRouter} from "react-router-dom";
import {connect} from 'react-redux';
import Home from './Common/HomeComponent';
import Register from "./Common/Register";
import RegisterForm from "./Common/RegisterForm";
import AccountActivationComponent from "./Common/AccountActivationComponent";


class Main extends Component{
    constructor(props) {
        super(props);
        this.state={
            user: this.props.session.user
        };
    };

    render(){
        return(
            <div>
                <BrowserRouter>
                    <Switch>
                        <Route exact path="/" component={() => <Home/>} />
                        <Route exact path="/register" component={() => <Register/>} />
                        <Route exact path="/register/:user" component={RegisterForm}/>
                        <Route exact path="/account/activation/:type_account/:activation_token"
                               component={AccountActivationComponent}/>
                        <Route exact path="/login" />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }

}


const mapStateToProps = state =>({session: state.session});
export default connect(mapStateToProps)(withRouter(Main));