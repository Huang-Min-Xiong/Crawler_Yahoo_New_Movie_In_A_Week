#### 安裝所需套件
`pip install -r requirements.txt`

#### 透過csv套件來實作功能
- encoding='utf-8-sig': 防止亂碼
- csv_writer = csv.writer(): 建立CSV檔寫入器
- csv_writer.writerow(): 寫入一列資料

#### 透過requests套件來實作功能
- requests.get(): 向網頁發送請求

#### 透過BeautifulSoup套件來實作功能
- soup = BeautifulSoup(): 解析網頁
- soup.find_all(): 搜尋所有節點

#### 執行結果
![image](https://github.com/MinXiong-Huang/Crawler_Yahoo_New_Movie_In_A_Week/blob/master/img/Result.PNG)
