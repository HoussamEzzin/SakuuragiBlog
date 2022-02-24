import logo from './logo.svg';
import './App.css';
import "bootstrap/dist/css/bootstrap.min.css";
import React, {useEffect} from 'react';
import {BrowserRouter} from "react-router-dom";
import {Provider} from 'react-redux';
import {BreakpointProvider} from "react-socks";
import {ConfigureStore} from "./Redux/ConfigureStore";
import Main from './Pages/MainComponent';

const store = ConfigureStore();

function App() {
  return (
    <Provider store={store}>
        <BreakpointProvider>
            <BrowserRouter>
                <Main />
            </BrowserRouter>
        </BreakpointProvider>
    </Provider>
  );
}

export default App;
