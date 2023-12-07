import streamlit as st
import time
from database import add_user, user_exists_by_name

def main():
    st.title("Registration Page")
    
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password', key="register_password")
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Register", key="register_submit_button"):
        if username and email and password and confirm_password:
            if password == confirm_password:
                if user_exists_by_name(username):
                    st.error("Error: Username already exists")
                else:
                    add_user(username, email, password)

                    st.success("User {} has been successfully registered.".format(username))
                    time.sleep(2)
                    st.session_state.clear()
                    st.session_state.page = "Login"
                    st.experimental_rerun()
            else:
                st.error("Error: Passwords do not match")
        else:
            st.error("All fields are required.")

    if st.button("Back to Login", key="back_to_login_button"):
        st.session_state.page = "Login"
        st.session_state.pop('password', None)
        st.experimental_rerun()

if __name__ == "__main__":
    main()
