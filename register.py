import streamlit as st

def main():
    st.title("Registration Page")
    
    menu = ["Home", "Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice != "Register":
        st.session_state.page = choice
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')

    if st.button("Register"):
        if password == confirm_password:
            st.success("User {} has been successfully registered.".format(username))
        else:
            st.error("Error: Passwords do not match")

if __name__ == "__main__":
    main()
