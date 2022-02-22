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

export const Session = (state=initialState,action) => {
    switch (action.type){
        case ActionTypes.LOGOUT:
            storage.remove("session_user");
            return {
                authenticated: false,
                user:null,
            };
        case ActionTypes.LOGIN:
            if(!action.error){
                user = action.payload.user;
                user.token = action.payload.token;
                storage.set("session_user",user);
                return {user, authenticated: true};
            }
            return {...state, user, authenticated: false};

    }
}