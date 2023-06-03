#多選按鈕   st.radio
import streamlit as st

genre = st.radio("您最喜歡的節目是甚麼?",('卡通', '戲劇', '愛情'))

if genre == '卡通':
    st.write('您選擇的是卡通')
elif genre == '戲劇':
    st.write('您選擇的是戲劇')
elif genre == '愛情':
    st.write('您選擇的是愛情')   