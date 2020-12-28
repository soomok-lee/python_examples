import os
import requests
from bs4 import BeautifulSoup

def get_dir_list(dir):
    str_list = ""
    if os.path.exists(dir):
        file_list = os.listdir(dir)
        file_list.sort()
        for f in file_list:
            full_path = os.path.join(dir, f)
            if os.path.isdir(full_path):
                f = "[" + f + "]"
            str_list += f
            str_list += "\n"
    str_list.strip()
    return str_list

def get_weather(where):
    weather = ""

    url = "https://search.naver.com/search/naver?query={}+날씨".format(where)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    w_box = bs.select("div.today_area > div.main_info")

    # print(w_box)

    if len(w_box) > 0:
        temperature = bs.select("span.todaytemp")
        cast_text = bs.select("p.cast_txt")
        indicator = bs.select("span.indicator")

        if len(temperature) > 0 and len(cast_text) > 0 and len(indicator) > 0:
            temperature = temperature[0].text.strip()
            cast_text = cast_text[0].text.strip()
            indicator = indicator[0].text.strip()
            
            weather = "{}\r\n{}\r\n{}".format(temperature, cast_text, indicator) 
    return weather

if __name__ == "__main__": # python module.py 시 실행
    get_weather("서울")