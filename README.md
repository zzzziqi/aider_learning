# Streamlit Login System

This repository contains a simple login system built with Streamlit and SQLite.

## How to use

1. Clone the repository.
2. Install the required packages using pip:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   streamlit run home.py
   ```

The application includes a login page, a registration page, and a welcome page. Users can register with a username, email, and password. The user data is stored in a SQLite database.

The login system uses Streamlit's session state to manage user sessions. When a user logs in, their username is stored in the session state. The username is then used to personalize the welcome page.

The application also includes a home page that displays all user data stored in the database.

## Note

This is a simple login system intended for educational purposes. It does not include any form of password encryption or user authentication. Use at your own risk.
