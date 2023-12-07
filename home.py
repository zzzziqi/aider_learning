import streamlit as st
import streamlit_session_state as session_state
from login import main as login_main
from register import main as register_main

def main():
    st.title("Home Page")

    menu = ["Home", "Login", "Register"]
    state = session_state.get(page="")
    if state.page == "Register":
        choice = "Register"
        state.page = ""
    else:
        choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        login_main()
    elif choice == "Register":
        register_main()

if __name__ == "__main__":
    main()
