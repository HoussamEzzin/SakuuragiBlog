import {createStore,combineReducers,applyMiddleware,compose} from "redux";
import * as objects from './Objects';
import promiseMiddleware from 'redux-promise';


export const ConfigureStore = () => {
    const composeEnhancers =  compose;

    const store = createStore(
        combineReducers({
            session: objects.Session,
            reader: objects.Reader,
            data: objects.Data,
        }),
        composeEnhancers(
            applyMiddleware(promiseMiddleware)
        )
    );

    return store;
}