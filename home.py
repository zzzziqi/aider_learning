import streamlit as st
from login import main as login_main
from register import main as register_main
from database import create_connection

def main():
    create_connection()
    if "page" not in st.session_state:
        st.session_state.page = "Home"
    st.title("Home Page")
    
    if st.sidebar.button("Home", key="home_button"):
        st.session_state.page = "Home"
    if st.sidebar.button("Login", key="login_button"):
        st.session_state.page = "Login"
    if st.sidebar.button("Register", key="register_button"):
        st.session_state.page = "Register"


    if st.session_state.page == "Home":
        st.subheader("Home")
    elif st.session_state.page == "Login":
        login_main()
    elif st.session_state.page == "Register":
        register_main()

if __name__ == "__main__":
    main()
