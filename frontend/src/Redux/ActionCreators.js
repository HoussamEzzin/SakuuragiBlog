import {createAction} from "redux-actions";
import * as types from './ActionTypes';
import {
    get_articles,
    add_article,
    delete_article,
} from "../Services/Api";

export const DeleteArticle = createAction(types.DELETE_ARTICLE, async obj => {
    return await delete_article(obj);
});

export const AddArticle = createAction(types.ADD_ARTICLE, async obj => {
    return await add_article(obj);
});

export const getArticles = createAction(types.GET_ARTICLES, async obj => {
    return await get_articles(obj);
})