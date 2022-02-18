import React, {Component} from "react";
import {BrowserRouter, Switch, Route, withRouter} from "react-router-dom";
import {connect} from 'react-redux';
import Home from './Common/HomeComponent';


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
                        <Route path="/" component={() => <Home/>} />
                    </Switch>
                </BrowserRouter>
            </div>
        )
    }

}


const mapStateToProps = state =>({session: state.session});
export default connect(mapStateToProps)(withRouter(Main));