import {createAction} from "redux-actions";
import * as types from './ActionTypes';
import {
    get_articles,
    add_article,
    delete_article,
    reader_register,
    partial_update_reader,
    login,
    reset_password,
    reset_password_edit,
    partial_update,
    logout,
    account_activation,
    get_publishers,
    publisher_register, get_publisher_articles, get_all_publisher
} from "../Services/Api";


export const loginAction = createAction(types.LOGIN, async obj => {
    return await login(obj);
});

export const resetPwdAction = createAction(types.RESETPASSWORD, async obj => {
    return await reset_password(obj);
});

export const resetPwdEditAction = createAction(types.RESETPASSWORDEDITE, async obj =>{
    return await reset_password_edit(obj);
});

export const partial_updateAction = createAction(types.PARTIALUPDATE, async obj =>{
    return await partial_update(obj);
});

export const logoutAction = createAction(types.LOGOUT, async () =>{
    return await logout();
});

export const accountActivationAction = createAction(types.ACTIVATION, async obj =>{
    return await account_activation(obj);
});

export const getPublishersAction = createAction(types.GETPUBLISHERS, async obj=>{
    return await get_publishers(obj);
})



export const deleteArticle = createAction(types.DELETE_ARTICLE, async obj => {
    return await delete_article(obj);
});

export const addArticle = createAction(types.ADD_ARTICLE, async obj => {
    return await add_article(obj);
});

export const getArticles = createAction(types.GET_ARTICLES, async obj => {
    return await get_articles(obj);
});

//Reader

export const readerRegisterAction = createAction(types.READERREGISTER, async obj =>{
    return await reader_register(obj);
});

export const partial_update_readerAction = createAction(types.PARTIALUPDATEREADER, async obj => {
    return await partial_update_reader(obj);
});

//Publisher

export const publisher_registerAction = createAction(types.PUBLISHERREGISTER, async obj =>{
    return await publisher_register(obj);
});

export const get_publisher_articlesAction = createAction(types.PUBLISHERARTICLES, async obj=>{
    return await get_publisher_articles(obj);
});

export const get_all_publishersAction = createAction(types.GETALLPUBLISHERS, async obj =>{
    return await get_all_publisher(obj);
});





