import streamlit as st
import streamlit_session_state as session_state

def main():
    st.title("Login Page")
    username = st.text_input("Username/Email")
    password = st.text_input("Password", type='password')

    col1, col2 = st.columns(2)
    if col1.button("Login"):
        st.success("Logged in as {}".format(username))
    if col2.button("Register"):
        state = session_state.get(page="")
        state.page = "Register"

if __name__ == "__main__":
    main()
