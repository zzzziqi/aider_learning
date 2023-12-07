import streamlit as st

def main():
    st.title("Welcome Page")
    st.write(f"Hello {st.session_state.username}")

if __name__ == "__main__":
    main()
