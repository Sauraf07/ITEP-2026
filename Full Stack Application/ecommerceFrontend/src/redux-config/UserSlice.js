import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
  name: "user",
  initialState: {
    isLoggedIn: false,
    currentUser: null,
  },
  reducers: {
    setUser: (state, action) => {
      state.currentUser = action.payload;
      state.isLoggedIn = true;
    },
    signOut: (state) => {
      state.currentUser = null;
      state.isLoggedIn = false;
    },
  },
});

export const { setUser, signOut } = userSlice.actions;
export default userSlice.reducer;
