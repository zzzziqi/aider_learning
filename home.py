import streamlit as st
from login import main as login_main
from register import main as register_main
from welcome import main as welcome_main

from database import create_connection, get_all_users, user_exists_by_name, add_user, get_user_email


def main():
    create_connection()
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    if st.sidebar.button("Home"):
        st.session_state.page = "Home"
        st.experimental_rerun()
    if st.sidebar.button("Login"):
        st.session_state.page = "Login"
        st.experimental_rerun()
    if st.sidebar.button("Register"):
        st.session_state.page = "Register"
        st.experimental_rerun()
    if 'username' in st.session_state:
        if st.sidebar.button("Welcome"):
            st.session_state.page = "Welcome"
            st.experimental_rerun()

    if st.session_state.page == "Home":
        st.title("Home Page")
        st.subheader("Home")
        if 'username' in st.session_state:
            email = get_user_email(st.session_state.username)
            st.write(f"You are logged in as {st.session_state.username}, Email: {email}")
        else:
            st.write("You are not logged in.")
        users = get_all_users()
        for user in users:
            st.write(f"Username: {user[0]}, Email: {user[1]}, Password: {user[2]}")
    elif st.session_state.page == "Login":
        login_main()

    elif st.session_state.page == "Welcome":
        welcome_main()
    elif st.session_state.page == "Register":
        register_main()

    if not user_exists_by_name("zzq"):
        add_user("zzq", "zzq@qq.com", "qqz")


if __name__ == "__main__":
    main()
