const { configureStore } = require("@reduxjs/toolkit");
import CounterSlice from "./CounterSlice";
import TodoSlice from "./TodoSlice";
const store = configureStore({
    reducer: {
        ConterData: CounterSlice,
        Todos : TodoSlice
    }
})
export default store;