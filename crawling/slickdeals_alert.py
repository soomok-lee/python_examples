import requests
from bs4 import BeautifulSoup
import json
import time

KAKAO_TOKEN = "Fpbk2jWKCgIRWodZZzsOdr_ML5jSBNoSF-O4VQorDNMAAAF2Z9AlbA"

def send_kakao(text):
    header = {"Authorization" : "Bearer " + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type":"text",
        "text": text,
        "link":{
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title":"go check right now!"
    }
    data = {"template_object": json.dumps(post)}
    r = requests.post(url, headers=header, data=data)

def get_hotdeal(query):
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}&pp=20".format(query)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    rows = bs.select("div.resultRow")

    results = []
    for r in rows:
        link = r.select("a.dealTitle")[0]
        href = link.get("href") # None 가능
        if href is None:
            continue
        href = "https://slickdeals.net" + href
        title = link.text
        price = r.select("span.price")[0].text.replace("$", "").replace("from", "").strip()
        if price.find("/") >= 0 or price == "":
            continue
        price = float(price)

        hot = len(r.select("span.icon-fire"))
        if hot > 0:
            results.append((title, href, price, hot))
    
    return results

send_lists =[]
def main():
    query = "ipad"
    max_price = 300.0
    while True:
        results = get_hotdeal(query)
        if results is not None:
            for r in results:
                title, href, price, hot = r
                if price < max_price:
                    if title not in send_lists:
                        msg = "{} {} {} {}".format(title, price, hot, href)
                        send_kakao(msg)
                        send_lists.append(title)
        time.sleep(60 * 5)

main()