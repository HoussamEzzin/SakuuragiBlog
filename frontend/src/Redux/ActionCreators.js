import {createAction} from "redux-actions";
import * as types from './ActionTypes';
import {
    get_articles,
    add_article,
    delete_article,
    login, reset_password, reset_password_edit
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

export const partial_updateAction = createAction()


export const deleteArticle = createAction(types.DELETE_ARTICLE, async obj => {
    return await delete_article(obj);
});

export const addArticle = createAction(types.ADD_ARTICLE, async obj => {
    return await add_article(obj);
});

export const getArticles = createAction(types.GET_ARTICLES, async obj => {
    return await get_articles(obj);
})