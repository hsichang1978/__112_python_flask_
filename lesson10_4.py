#下拉式選單 selectbox
import streamlit as st

option = st.selectbox('您選擇的聯絡方式?',('郵件', '市話', '行動電話'))

st.write('您選擇:', option)


