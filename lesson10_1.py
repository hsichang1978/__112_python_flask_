import streamlit as st

def button_click():
    st.write(st.session_state)

if st.button("say Hello!",key='myButton',on_click=button_click):          #streamlit st.button
    #on_click，當button被按下時，要執行甚麼程式。此範例為button按下後顯示專案記憶體內myButton內的True或False
    st.write("Why hello there")
else:
    st.write("Goodbye")

