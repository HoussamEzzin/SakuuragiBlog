import {createStore,combineReducers,applyMiddleware,compose} from "redux";

import promiseMiddleware from 'redux-promise';


export const ConfigureStore = () => {
    const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

    const store = createStore(
        combineReducers({

        }),
        composeEnhancers(
            applyMiddleware(promiseMiddleware)
        )
    );

    return store;
}