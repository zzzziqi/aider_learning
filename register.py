import streamlit as st
from database import add_user, user_exists_by_name

def main():
    st.title("Registration Page")
    
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Register", key="register_submit_button"):
        if password == confirm_password:
            if user_exists_by_name(username):
                st.error("Error: Username already exists")
            else:
                add_user(username, email, password)
import time

                st.success("User {} has been successfully registered.".format(username))
                st.session_state.register_time = time.time()
                if 'register_time' in st.session_state and time.time() - st.session_state.register_time > 2:
                    st.session_state.page = "Login"
                    st.experimental_rerun()
        else:
            st.error("Error: Passwords do not match")

if __name__ == "__main__":
    main()
