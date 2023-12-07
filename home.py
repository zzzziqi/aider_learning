import streamlit as st
from login import main as login_main
from register import main as register_main

def main():
    st.title("Home Page")

    menu = ["Home", "Login", "Register"]
    if "page" in st.session_state and st.session_state.page == "Register":
        choice = "Register"
        st.session_state.page = ""
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
