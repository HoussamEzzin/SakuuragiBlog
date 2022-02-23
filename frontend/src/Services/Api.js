import axios from "axios";
import {ConfigureStore} from "../Redux/ConfigureStore";
import {get} from "./Storage";

require('dotenv').config()
const instance = axios.create({baseURL: process.env.REACT_APP_API_KEY});

const store = ConfigureStore().getState();

console.log("store"+store.session)

//to get auth token
const user = get("session_user")


// manage all kind of erros

const mapRegisterError = response => {
    if (response.data.message === "Username already exist!") {
        return "Username already exist"
    }
    if (response.data.username) {
        if (response.data.username[0] === "This field is required.") {
            return "Error sending data"
        }
        if (response.data.username[0] === "This field is required.") {
            return "Error sending data"
        }
    }
    if (response.data.email) {
        if (response.data.email[0] === "This field is required.") {
            return "Error sending data"
        }
        if (response.data.email[0] === "user with this email already exists.") {
            return "User with this email already exists"
        }
        if (response.data.username[0] === "This field is required.") {
            return "Error sending data"
        }
    }
    return response.data;
};
const mapPublisherRegisterError = response => {
    if (response.data.message === "Username already exist!") {
        return "Username already exist"
    }
    if (response.data.username) {
        if (response.data.username[0] === "This field is required.") {
            return "Error sending data"
        }
        if (response.data.username[0] === "This field is required.") {
            return "Error sending data"
        }
    }
    if (response.data.email) {
        if (response.data.email[0] === "This field is required.") {
            return "Error sending data"
        }
        if (response.data.email[0] === "user with this email already exists.") {
            return "User with this email already exists"
        }
        if (response.data.username[0] === "This field is required.") {
            return "Error sending data"
        }
    }
    return response.data;
};

const mapActivationError = response => {
    console.log(response)
    if (response.data.error === "Activation Expired") {
        return "Token Activation Expired"
    }
    if (response.data.error === "Invalid token") {
        return "Invalid Token Activation"
    }
    if (response.data.email === "Successfully activated") {
        return "Your account Successfully activated"
    }
    return response.data;
};

const mapAuthError = response => {
    if (response.data.message === "wrong username or password!") {
        return "Username or Password incorrect";
    }

    return response.data.message;
};

//Common

export const login = _data => {
    return instance
        .post("api/accounts/login/", JSON.stringify(_data))
        .then(response => {
            return response.data;
        })
        .catch(err=>{
            if(err.response){
                throw new Error(mapAuthError(err.response));
            }
            throw err;
        });
};

export const reset_password = _data => {
    return instance
        .post("api/reset_password/", JSON.stringify(_data))
        .then(response => {
            return response.data;
        })
        .catch(err => {
            if(err.response){
                throw new Error(mapAuthError(err.response));
            }
            throw err;
        });
};

export const reset_password_edit = _data => {
    return instance
        .post("api/reset_password/edit/", JSON.stringify(_data))
        .then(response => {
            return response.data;
        })
        .catch(err => {
            if(err.response){
                throw new Error(mapAuthError(err.response));
            }
            throw err;
        });
};

export const partial_update = _data => {
    const user = get("session_user");
    return instance
        .put(`api/accounts/update-partial/${user.id}/`, JSON.stringify(_data), {
            headers: {Authorization: "Token" + user.token}
        })
        .then(response=>{
            return response.data;
        })
        .catch(err => {
            if(err.response){
                throw new Error(mapAuthError(err.response));
            }
            throw err;
        });
};


// publisher

export const publisher_register = _data => {
    return instance
        .post("api/accounts/publisher/register/", _data)
        .then(response => {
            return response.data;
        })
        .catch(err => {
            if(err.response){
                throw new Error(mapPublisherRegisterError(err.response));
            }
            throw err;
        });
};

export const get_publisher_articles = _data=>{
    const user = get("session_user");
    return instance
        .get(`api/accounts/publisher/articles/${_data.publisher_id}/`,{
            headers: {Authorization: "Token" + user.token}
        })
        .then(response => {
            return response.data;
        })
        .catch(err=>{
            if(err.response){
                throw new Error(mapPublisherRegisterError(err.response));
            }
            throw err;
        })
}



//Api articles

export const get_articles = () =>{
    return instance.get("api/get/articles/")
        .then(response => {
            return response.data;
        })
        .catch(err=>{
            if(err.response){
                throw new Error(mapRegisterError(err.response));
            }
            throw err;
        });
};


export const add_article = _data =>{
    const user = get("session_user");
    return instance
        .post("api/accounts/articles/add_article/", _data, {
            headers: {Authorization: "Token" + user.token}
        })
        .then(response=>{
            return response.data;
        })
        .catch(err => {
            if(err.response){
                throw new Error(mapPublisherRegisterError((err.response)));
            }
            throw err;
        });
};

export const add_article_picture = (data) => {
    const user = get("session_user");
    return instance
        .put(`api/accounts/articles/add_article_picture/${data.id}`, data.data, {
            headers: { Authorization: "Token" + user.token}
        })
        .then(response=>{
            return response.data;
        })
        .catch(err => {
            if(err.response){
                throw new Error(mapAuthError((err.response)));
            }
            throw err;
        });
};


export const delete_article = id => {
    let token = user.token
    return instance
        .delete(`api/delete/article/${id}`,{
            headers : {Authorization : "Token " + token}
        })
        .then(response => {
            return response.data;
        })
        .catch(err => {
            // if (err.response){
            //     throw new
            // }
            throw err;
        });
}