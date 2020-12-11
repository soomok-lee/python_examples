'''
crawling order

1. 원하는 웹페이지에 접속하여 HTML 데이터를 받아온다.
2. 받아온 HTML 데이터를 분석가능한 형태로 가공한다.
3. 원하는 데이터를 추출한다.

requests, requests_html, BeautifulSoup4
pip install requests
pip install requests_html
pip install BeautifulSoup4
'''
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession

# response = requests.get("https://www.naver.com")
# print(response.status_code)
# print(response.headers)
# print(response.text) # decoded content

response = requests.get("https://www.naver.com")
bs = BeautifulSoup(response.text, "html.parser")
for img in bs.select("img"):
    print(img)
for a in bs.select("a"):
    print(a)

# session = HTMLSession()
# response = session.get("https://www.naver.com")
# print(response.html.links)