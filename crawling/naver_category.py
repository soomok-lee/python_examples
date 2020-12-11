import requests
from bs4 import BeautifulSoup
import time

# r = requests.get("https://www.naver.com")
# bs = BeautifulSoup(r.text, "html.parser")

# lists = bs.find_all("li", {"class": "category_item"})
# for li in lists:
#     title = li.find("a").text # text:  tag <></> 사이 내용
#     print(title)

'''
li.클래스   
li#아이디
'''
# lists = bs.select("li.category_item") 
# for li in lists:
#     title = li.select("a")[0].text # select - return list
#     print(title)


# lxml
'''
pip install lxml # parser보다 속도가 빠름
'''
def time_function(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} {} time {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper

@time_function
def r_find_all(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.find_all("li.category_item") 
    
    titles = []
    for li in lists:
        title = li.select("a")[0].text # select - return list
        titles.append(title)
    return titles

@time_function
def r_select(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.select("li.category_item") 
    
    titles = []
    for li in lists:
        title = li.select("a")[0].text # select - return list
        titles.append(title)
    return titles

url = "https://www.naver.com"
r_find_all(url, "html.parser")
r_select(url, "html.parser")
r_find_all(url, "lxml")
r_select(url, "lxml")

