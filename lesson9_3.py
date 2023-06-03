
# st.metric 粗體顯示指標，並可選指示指標如何變化
# st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")
import streamlit as st

st.metric(label="溫度", value="70 °F", delta="-1.2 °F")