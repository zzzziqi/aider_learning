import streamlit as st

def main():
    st.title("Login Page")
    username = st.text_input("Username/Email")
    password = st.text_input("Password", type='password')

    if st.button("Login"):
        st.success("Logged in as {}".format(username))
    if st.button("Register"):
        st.info("Please go to the Register page to create an account.")

if __name__ == "__main__":
    main()
