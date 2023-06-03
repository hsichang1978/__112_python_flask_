#text_input讓使用者可以輸入文字
import streamlit as st
import datetime

title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

#number_input讓使用者可以輸入數字
number = st.number_input('Insert a number')
st.write('The current number is ', number)


#date_input讓使用者可以輸入日期
d = st.date_input("When\'s your birthday",datetime.date(2019, 7, 6))
st.write('Your birthday is:', d)