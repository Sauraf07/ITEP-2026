import { createSlice } from "@reduxjs/toolkit";

const counterSlice = createSlice({
    name: "counter",
    initialState: {
        count : 100,
        evenCounter : 0,
        oddCounter : 1
    },
    reducers: {
        increment : (state) => {state.count += 1},
        incevenCounter : (state) => {state.evenCounter += 2},
        incoddCounter : (state) => {state.oddCounter += 2}
    }
})


export const {increment, incevenCounter, incoddCounter} = counterSlice.actions;
export default counterSlice.reducer;