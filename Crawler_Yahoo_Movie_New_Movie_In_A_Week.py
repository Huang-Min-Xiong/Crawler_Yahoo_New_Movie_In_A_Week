import csv
import requests
from bs4 import BeautifulSoup
 
url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
info_items = soup.find_all('div', 'release_info')
 
#encoding='utf-8-sig':防止亂碼
with open(r'.\Crawler_Yahoo_Movie_New_Movie_In_A_Week.csv', 'w', encoding='utf-8-sig', newline='') as csv_file:    
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['中文片名', '英文片名', '上映時間', '網友期待度'])
 
    for item in info_items:
        Movie_Ch_Name = item.find('div', 'release_movie_name').a.text.strip() #中文片名        
        Movie_En_Name = item.find('div', 'en').a.text.strip() #英文片名
        Date = item.find('div', 'release_movie_time').text.split('：')[-1].strip() #上映時間
        Expect = item.find('div', 'leveltext').span.text.strip() #網友期待度
        
        print('{}({}) 上映時間：{} 網友期待度：{}'.format(Movie_Ch_Name, Movie_En_Name, Date, Expect))
        csv_writer.writerow([Movie_Ch_Name, Movie_En_Name, Date, Expect]) #寫入CSV檔
