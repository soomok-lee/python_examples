'''
pip install Flask
Flask? python web development
'''
import requests
from bs4 import BeautifulSoup
import re

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__) # Flask 객체 생성하여 app 변수에 저장

def search_google(keyword, start_page, end_page=None):
    url = "https://www.google.com/search?q={0}+magnet%3A%3Fxt%3D&oq={0}+magnet%3A%3Fxt%3D&start={1}".format(keyword, start_page)
    header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36,gzip(gfe)"}
    r = requests.get(url, headers=header)       
    bs = BeautifulSoup(r.text, "lxml")
    links = bs.select("div.g > div.rc > div.yuRUbf > a")

    results = []

    if end_page is None:
        # 페이징 될 경우 '2 of about 4830000 results (0.28 seconds)' 이런 형식으로 결과가 출력됩니다.
        # 그래서 "of about" 과 "results" 사이의 결과 갯수를 파싱하기 위해서 아래처럼 작업합니다.
        parse_text_1 = "of about"
        parse_text_2 = "results"
        # 최초의 검색 결과를 div 태그의 ID가 result-stats 인 요소의 text 값을 구합니다.
        text = bs.select("div#result-stats")[0].text

        text = text[text.find(parse_text_1) + len(parse_text_1):]
        text = text[:text.find(parse_text_2)]
        counts = text.replace(",", "").strip()

        end_page = int(int(counts) / 10)
        if end_page > 20:
            end_page = 20

    for a in links:
        href = a["href"]
        text = a.select("h3")
        if len(text) <= 0:
            continue
        title = text[0].text

        try:
            r = requests.get(href)       
            bs = BeautifulSoup(r.text, "lxml")
            magnets = bs.find_all("a", href=re.compile(r'magnet:\?xt=*'))

            if len(magnets) > 0:
                magnet = magnets[0]["href"]
                results.append({
                    "magnet": magnet,
                    "title": title
                })
        except:
            pass
    
    if start_page < end_page:
        start_page += 10
        results.extend(search_google(keyword, start_page, end_page=end_page))
    
    return results

@app.route("/", methods=["GET", "POST"])
def index():
    if "keyword" in request.form:
        keyword = request.form["keyword"] # form - value
        results = search_google(keyword, 0)
    else:
        results = []

    if len(results) > 0:
        return render_template("index.html", **{"magnets" : results}) # **kwargs
    else:
        return render_template("index.html") # templates/index.html
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True) # localhost:8080
    # windows 'netstat -na'로 열려있는 포트 확인 가능