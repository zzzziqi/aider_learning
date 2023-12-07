import streamlit as st
from login import main as login_main
from register import main as register_main

def main():
    st.title("Home Page")
    
    if st.sidebar.button("Home"):
        st.session_state.page = "Home"
    if st.sidebar.button("Login"):
        st.session_state.page = "Login"
    if st.sidebar.button("Register"):
        st.session_state.page = "Register"


    if st.session_state.page == "Home":
        st.subheader("Home")
    elif st.session_state.page == "Login":
        login_main()
    elif st.session_state.page == "Register":
        register_main()

if __name__ == "__main__":
    main()
