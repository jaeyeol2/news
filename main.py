import pandas as pandas
import requests as requests
from PyNaver import Naver
from sqlalchemy import create_engine
# import pandas as pd
# from bs4 import BeautifulSoup
# import requests
# import MySQLdb
# from sqlalchemy.dialects.mssql.information_schema import columns
# import pymysql

client_id = "pap20qDk3bNNGol3EczS"
client_secret = "2sEZKsNWnU"

url = "https://openapi.naver.com/v1/search/news.xml?query="

naver = Naver(client_id, client_secret)
query = "코로나 확진자" # 검색
display = '10' # 출력 수
sort = "sim"

df = naver.search_news(query=query, display=display, sort=sort)
df.head()
print(type(df))

MYSQL_HOSTNAME = '192.168.131.20:3306'  # 내 mysql ip
MYSQL_USER = 'test'  # 내가 생성한 user
MYSQL_PASSWORD = 'qwer1234'
MYSQL_DATABASE = 'test_db'   # 내가 생성한 db

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'

db = create_engine(connection_string)

df = df.astype({"pubDate": "datetime64"}) # 날짜데이터 타입변경

df.to_sql(name='news', con=db, if_exists = 'replace', index= False)
# if_exists
# replace = 기존데이터 삭제후 새로운데이터 갱신
# append = 기존데이터 위에 덮어쓰기
db.execute('ALTER TABLE news ADD COLUMN id INT(9) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST;')