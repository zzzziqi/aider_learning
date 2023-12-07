import streamlit as st
from aider.database import user_exists

def main():
    st.title("Login Page")
    
    username = st.text_input("Username/Email")
    password = st.text_input("Password", type='password')

    col1, col2 = st.columns(2)
    if col1.button("Login", key="login_submit_button"):
        if user_exists(username, password):
            st.success("Logged in as {}".format(username))
        else:
            st.error("Invalid username or password")
    if col2.button("Register", key="login_register_button"):
        st.session_state.page = "Register"
        st.experimental_rerun()

if __name__ == "__main__":
    main()
