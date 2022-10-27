# 抓取 PTT 新竹版的網頁原始碼(HTML)
import urllib.request as req
import json

url= "https://www.ptt.cc/bbs/Hsinchu/index.html" # 可以換成想要抓的PTT版之網址
# 建立一個 Request 物件，附加 Request Headers 的資訊(看起來像人類)
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")
# 解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
titles=root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤
for title in titles:
    if title.a !=None: # 如果標題包含 a 標籤(仍存在於網頁上)，就印出來
        finish = title.a.string 
        json_dict = json.dumps(finish,ensure_ascii=False).encode('utf8')
        decode = json_dict.decode()
        print(decode)

# 轉為csv檔
temp = []
for title in titles:
    if title.a !=None: # 如果標題包含 a 標籤(仍存在於網頁上)，就印出來
        finish = title.a.string 
        json_dict = json.dumps(finish,ensure_ascii=False).encode('utf8')
        decode = json_dict.decode()
        temp.append(decode)
        print(decode)
# 確認temp裡面有沒有東西
print(temp)
# 轉換成 DataFrame
import pandas as pd
df = pd.DataFrame(temp)
print(df)
# 轉為csv檔，直接下載
# 轉為csv檔並下載
df.to_csv('Hsinchu_PTT.csv')
print("csv下載完成")


# 將 DataFrame 轉為 Dictionary

## 確認現在 temp 的 type
temp = df.to_dict()
type(temp)
# 將 Dictionary 轉成 json檔並下載
with open('Hsinchu_PTT.json', 'w', encoding='utf-8') as file:
    json.dump(temp, file, ensure_ascii=False)  

print("json下載完成")
