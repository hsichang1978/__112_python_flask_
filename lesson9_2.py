import numpy as np
import pandas as pd
import streamlit as st

scores_array = np.random.randint(50,high=101,size=(50,5))
student_dataFrame = pd.DataFrame(data=scores_array,columns=["國文","英文","數學","地理","社會"],index=range(1,51))
# print(student_dataFrame)

st.header("3年5班成績表")
# st.table(data=student_dataFrame)
#st.table(data=None)  streamlit表格是靜態的：其全部內容直接佈局在頁面上。

st.dataframe(data=student_dataFrame)    #表格有卷軸
#st.dataframe(data=None, width=None, height=None, *, use_container_width=False, hide_index=None, column_order=None, column_config=None)
# st.dataframe數據框顯示為交互式表格
