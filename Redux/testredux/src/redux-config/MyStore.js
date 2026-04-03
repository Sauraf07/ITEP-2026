import {configureStore} from "@reduxjs/toolkit";
import counterSlice from "./counter";

const store = configureStore({
    reducer : {
        counter : counterSlice
    }
});

export default store;