import streamlit as st
import time

st.set_page_config(
    page_title = "joke",
)

st.title("funny jokes")

button=st.button("click here for maximum enjoyment")

placeholder=st.empty()

if button:
    placeholder.write("joke?")
    time.sleep(2)
    placeholder.write("joke Q")
    time.sleep(5)
    placeholder.write("joke A")
    time.sleep(1)
    placeholder.audio(.wav,autoplay=true)

