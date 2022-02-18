import axios from "axios";
import {ConfigureStore} from "../Redux/ConfigureStore";
import {get} from "./Storage";

require('dotenv').config()
const instance = axios.create({baseURL: process.env.REACT_APP_API_KEY});

const store = ConfigureStore().getState();

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
}

// TODO : change this function (only publishers are allowed to publish)
export const add_article = _data =>{
    return instance
        .post("api/add/article/",
            _data, )
        .then(response =>{
            return response.data
            }
        )
        .catch(err => {
            // if(err.response){
            //     throw new Error()
            // }
            throw err;
        })
}