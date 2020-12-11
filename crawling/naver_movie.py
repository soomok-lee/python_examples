import requests
from bs4 import BeautifulSoup
# pip install openpyxl # excel
import pandas # pip install pandas

def get_movie_point(start, end): # page start~end
    results = []

    for i in range(start, end + 1):
        url = "https://movie.naver.com/movie/point/af/list.nhn?&page={}".format(i)

        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")

        trs = bs.select("table.list_netizen > tbody > tr") # ' > ' 띄어쓰기 필수
        for tr in trs:
            # number
            number = tr.select_one("td.ac.num").text
            # author
            author = tr.select_one("td.num > a.author").text
            # print("{} {}".format(number, author))
            
            # td class="title"
            tr_data = tr.select_one("td.title")
            # title
            # td class="title" - first <a> - text
            title = tr_data.select_one("a").text
            # point
            # td class="title" - <div> - <em> - score
            point = tr_data.select_one("div.list_netizen_score > em").text
        
            # td class="title" - extract() <a>, <div>, <br>
            # [x.extract() for x in tr_data.select("a")]
            # [x.extract() for x in tr_data.select("div")]
            # [x.extract() for x in tr_data.select("br")]

            # 위에서 태그를 모두 제거한 tr_data에서 내용만 추출
            # content = tr_data.text.strip()

            # results.append({
            #     "number":number,
            #     "author":author
            # })
            results.append([number, author, title, point])
    return results
            
# print(get_movie_point(1, 10))

column = ["number", "author", "title", "point"]
results = get_movie_point(1, 3)
dataframe = pandas.DataFrame(results, columns=column)
print(dataframe)
dataframe.to_excel("movie.xlsx", sheet_name="naver movie", header=True, startrow=1)