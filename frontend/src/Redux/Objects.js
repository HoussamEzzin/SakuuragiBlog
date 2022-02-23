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
        case ActionTypes.PARTIALUPDATE:
            if(!action.error){
                user = action.payload.user;
                user.token = action.payload.token
                storage.set("session_user",user);
                return {user, authenticated: true};
            }
            return {...state, user, authenticated: true};
        case ActionTypes.PARTIALUPDATEPUBLISHER:
            if(!action.error){
                user = action.payload.user;
                user.token = action.payload.token;
                storage.set("session_user", user);
                return {user, authenticated: true};
            }
            return {...state, user, authenticated: true};
        case ActionTypes.PARTIALUPDATEREADER:
            if(!action.error){
                user=action.payload.user;
                user.token = action.payload.token;
                storage.set("session_user", user);
                return {user, authenticated: true};
            }
            return {...state, user, authenticated: true};
        default:
            return state;

    }
}

export const Reader = ( state = {
    allPublishers:[],
    publisher:[],
    errMess:null,
    isLoad:false,
    }, action) => {
    switch (action.type){
        case ActionTypes.GETALLPUBLISHERS:
            if(!action.error){
                return{
                    ...state,
                    publishers: action.payload.publishers_list,
                    isLoad:true,
                };
            }
            return {...state, publishers: [], errMess: action.error};
        default:
            return state;
    }
}


export const Data = (state={
    publisher_articles: [],
    get_categories: [],
    get_all_articles: [],
    errMess:null,
    isLoad: false,
}, action) => {
    switch (action.type){
        case ActionTypes.PUBLISHERARTICLES:
            if(!action.error){
                return {
                    ...state,
                    publisher_articles: action.payload.publisher_article,
                    isLoad: true,
                }
            }
            //uncomplete
    }
}