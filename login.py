import streamlit as st

def main():
    st.title("Login Page")
    
    menu = ["Home", "Login", "Register"]
    choice = st.sidebar.selectbox("Menu", menu)
    if choice != "Login":
        st.session_state.page = choice
    username = st.text_input("Username/Email")
    password = st.text_input("Password", type='password')

    col1, col2 = st.columns(2)
    if col1.button("Login"):
        st.success("Logged in as {}".format(username))
    if col2.button("Register"):
        st.session_state.page = "Register"

if __name__ == "__main__":
    main()
