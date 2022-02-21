import * as ActionTypes from './ActionTypes';
import * as storage from "../Services/Storage";

const initialState = {
    user: storage.get("session_user"),
    authenticated: false
};

let user;

if(initialState.user){
    initialState.authenticated = true;
}

export