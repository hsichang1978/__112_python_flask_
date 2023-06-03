
import requests
import pandas as pd
import streamlit as st
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
response = requests.request('GET',url)
if response.status_code == 200:         
#屬性檢查，此屬性檢查響應的狀態代碼是否在 400 和 600 之間，以查看是否存在客戶端錯誤或服務器錯誤。如果狀態代碼在 200 到 400 之間，這將返回 True。
#丟回200數值，表連線成功
    print("連線成功")
    all_data = response.json()
    print(type(all_data))
else:
    print(f"連線失敗:{response.status_code}")


#pandas是一套能夠有效率的對資料進行篩選及分析的應用程式
dataFrame = pd.DataFrame(data=all_data,columns=['sna','tot','sbi','sarea','mday','ar','bemp','act'])
min = int(input("請輸入要查詢的可借數量:"))
mask = dataFrame['sbi'] <= min
mask_dataFrame = dataFrame[mask]
mask_dataFrame.to_csv('可借小於3的站點.csv')
filename = f'可借小於{min}的站點.xlsx'
mask_dataFrame.to_excel(filename)
