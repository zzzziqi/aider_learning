import streamlit as st
from database import user_exists

def main():
    st.title("Login Page")
    
    if 'username' in st.session_state:
        st.write(f"You are logged in as {st.session_state.username}")
        if st.button("Logout", key="logout_button"):
            st.session_state.clear()
            st.session_state.page = "Login"
            st.experimental_rerun()
    else:
        username = st.text_input("Username/Email")
        password = st.text_input("Password", type='password')

        col1, col2 = st.columns(2)
        if col1.button("Login", key="login_submit_button"):
            if user_exists(username, password):
                st.session_state.username = username
                st.session_state.page = "Welcome"
                st.experimental_rerun()
            else:
                st.error("Invalid username or password")
        if col2.button("Register", key="login_register_button"):
            st.session_state.page = "Register"
            st.session_state.pop('password', None)
            st.experimental_rerun()

if __name__ == "__main__":
    main()
