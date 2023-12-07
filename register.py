import streamlit as st
from database import add_user

def main():
    st.title("Registration Page")
    
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Register", key="register_submit_button"):
        if password == confirm_password:
            add_user(username, password)
            st.success("User {} has been successfully registered.".format(username))
        else:
            st.error("Error: Passwords do not match")

if __name__ == "__main__":
    main()
