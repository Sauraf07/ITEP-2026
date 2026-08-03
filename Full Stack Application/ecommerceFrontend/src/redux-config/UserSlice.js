import { createSlice } from "@reduxjs/toolkit";

const loadUserFromStorage = () => {
  try {
    const userStr = localStorage.getItem("user");
    if (userStr) {
      const user = JSON.parse(userStr);
      return {
        isLoggedIn: true,
        currentUser: user,
      };
    }
  } catch (e) {
    console.error("Error loading user from localStorage", e);
  }
  return {
    isLoggedIn: false,
    currentUser: null,
  };
};

export const userSlice = createSlice({
  name: "user",
  initialState: loadUserFromStorage(),
  reducers: {
    setUser: (state, action) => {
      state.currentUser = action.payload;
      state.isLoggedIn = true;
      localStorage.setItem("user", JSON.stringify(action.payload));
    },
    signOut: (state) => {
      state.currentUser = null;
      state.isLoggedIn = false;
      localStorage.removeItem("user");
    },
  },
});

export const { setUser, signOut } = userSlice.actions;
export default userSlice.reducer;
