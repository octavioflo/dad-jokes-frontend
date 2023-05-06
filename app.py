import streamlit as st
import requests

def display_header() -> None:
    st.image("img/dadjoke.png")
    st.title("Welcome to Dad Jokes")
    st.text("Click on the button below for a dad joke.")


def get_joke() -> dict:
    return requests.get("http://localhost:8000/joke").json()

def button() -> None:
    if st.button('Click Me'):
        joke = get_joke()
        st.write(f'*{joke["joke"]}*')
    

def main():
    display_header()
    button()

if __name__ == "__main__":
    main()