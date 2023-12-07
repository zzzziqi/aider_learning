import streamlit as st
from login import main as login_main
from register import main as register_main

def main():
    st.title("Home Page")
    
    menu = ["Home", "Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu, key="home_page_selectbox")
    if choice != "Home":
        st.session_state.page = choice


    if choice == "Home":
        st.subheader("Home")
    elif choice == "Login":
        login_main()
    elif choice == "Register":
        register_main()

if __name__ == "__main__":
    main()
