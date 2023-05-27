import requests
url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
response = requests.request('GET',url)
if response.status_code == 200:
    print("連線成功")
    print(response.text)    #text是屬性，不要用括號
#【json檔】是java的物件，為純文字複雜資料，有可能為list內，包含了dictionary。
#承上，dictionary內的value又包含了list，故稱純文字複雜資料。
else:
    print(f"連線失敗{response.status_cpde}")

