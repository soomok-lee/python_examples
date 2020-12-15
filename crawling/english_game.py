'''
https://www.usatoday.com/
위 사이트로 부터 영어 단어들을 크롤링하여 영어 게임 만들기
'''
import requests
from bs4 import BeautifulSoup
import re # 정규식
import json
import random
import os

def get_news():
    url = "https://www.usatoday.com"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")
    lists = bs.select("div.gnt_m_th > a.gnt_m_th_a")
    for li in lists:
        href = url + li["href"] # 해당 기사의 link

        r = requests.get(href)
        bs = BeautifulSoup(r.text, "lxml")
        texts = bs.select("div.gnt_ar_b > p.gnt_ar_b_p")
        contents = [p.text for p in texts]
        contents = " ".join(contents) # str
        return contents.lower()
    return None

news = get_news()

def naver_translate(word):
    try:
        url = "https://ac-dict.naver.com/enko/ac?st=11&q={}".format(word)
        r = requests.get(url)
        j = json.loads(r.text)
        return (j["items"][0][0][2][0])
    except:
        return None

def make_quiz(news):
    match_pattern = re.findall(r'\b[a-z]{4,15}\b', news) # 4글자 이상 15글자 미만의 단어

    frequency = {}
    quiz_list = []

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
        # print(frequency[word]) 

    for word, count in frequency.items():
        # print(word, count)
        if count > 1:
            kor =  naver_translate(word)
            if kor is not None:
                quiz_list.append({kor: word})
        
    return quiz_list

def quiz():
    news = get_news()
    quiz_list = make_quiz(news)
    random.shuffle(quiz_list)

    chance = 5
    count = 0
    for q in quiz_list:
        os.system("cls")
        count += 1 
        kor = list(q.keys())[0]
        english = q.get(kor)

        print("*" * 90)
        print("문제 : {}".format(kor))
        print("*" * 90)

        for j in range(chance):
            user_input = input("위의 뜻이 의미하는 단어를 입력하세요. : ").strip().lower()
            if user_input == english:
                print("정답입니다!! {} 문제 남았습니다.".format(len(quiz_list) - count))
                os.system("pause")
                break
            else:
                n = chance - (j + 1)
                if j == 0:
                    print("{} 가 아닙니다. {} 번 기회가 남았습니다.".format(user_input, n))
                elif j == 1:
                    print("{} 가 아닙니다. {} 번 기회가 남았습니다. 힌트: {}로 시작.".format(user_input, n, english[0]))
                elif j == 2:
                    hint = " _ " * int(len(english) - 2)
                    print("{} 가 아닙니다. {} 번 기회가 남았습니다. 힌트: {} {} {} 로 시작.".format(user_input, n, english[0], english[1], hint))
                elif j == 3:
                    hint = " _ " * int(len(english) - 3)
                    print("{} 가 아닙니다. {} 번 기회가 남았습니다. 힌트: {} {} {} {} 로 시작.".format(user_input, n, english[0], english[1], english[2], hint))
                else:
                    print("틀렸습니다. 정답은 {} 입니다.".format(english))
                    os.system("pause")
    
    print("더이상 문자가 없습니다.")
    
quiz()