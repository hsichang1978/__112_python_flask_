
import streamlit as st

agree = st.checkbox("我同意")
#checkbox會回傳布林值，預設布林值為【False】
if agree:
    st.write("great") 