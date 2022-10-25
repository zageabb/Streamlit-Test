import pickle
from pathlib import Path


import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth

st.set_page_config(
    page_title="Gerry's Multipage App",
    
)

names = ["Gerald Abbot", "Matthew Abbot"]
usernames = ["gabbot", "mabbot"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

credentials = {"usernames":{}}

for un, name, pw in zip(usernames, names, hashed_passwords):
    user_dict = {"name":name,"password":pw}
    credentials["usernames"].update({un:user_dict})

authenticator = stauth.Authenticate(credentials, "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status == True:
    authenticator.logout("logout","sidebar")  #main or sidebar

if authentication_status == True:
    st.title("Main Page")

    st.sidebar.success("Select a page above")

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""

    my_input = st.text_input("Input a text here", st.session_state["my_input"])
    submit = st.button("Submit")

    if submit:
        st.session_state["my_input"] = my_input
        st.write("You have entered:", my_input)

