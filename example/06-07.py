'''
06. 타이핑 게임 simple
총 글자 별 계산
'''
# import random
# import time
# import os

# WORD_LIST = [
#     "Python programming",
#     "Let's coding~",
#     "Merry Christmas!"
# ]

# random.shuffle(WORD_LIST)

# for q in WORD_LIST:
#     os.system("cls")
#     start_time = time.time()
#     user_input = str(input(q+'\n')).strip()
#     end_time = time.time() - start_time

#     if user_input == "/exit":
#         break

#     correct = 0
#     for i, c in enumerate(user_input):
#         if i >= len(q):
#             break
#         if c == q[i]:
#             correct += 1
    
#     tot_len = len(q)
#     c = correct / tot_len * 100
#     e = (tot_len - correct) / tot_len * 100
#     speed = (correct / end_time) * 60

#     print("speed : {:0.2f}, correct : {:0.2f}, typo : {:0.2f}".format(speed, c, e))
#     os.system("pause")

'''
07. 타이핑 게임 smart
총 타수 별 계산

한글 = ((초성 * 21) + 중성) * 28 + 종성 + 44032
초성 = ((x - 44032) / 28) / 21
중성 = ((x - 44032) / 28) % 21
종성 = (x - 44032) % 28
'''
import random
import time
import os

CHO = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"] # 초성
JUNG = ["ㅏ", "ㅐ", "ㅑ", "ㅒ", "ㅓ", "ㅔ", "ㅕ", "ㅖ", "ㅗ", "ㅘ", "ㅙ", "ㅚ", "ㅛ", "ㅜ", "ㅝ", "ㅞ", "ㅟ", "ㅠ", "ㅡ", "ㅢ", "ㅣ"] # 중성
JONG = ["", "ㄱ", "ㄲ", "ㄳ", "ㄴ", "ㄵ", "ㄶ", "ㄷ", "ㄹ", "ㄺ", "ㄻ", "ㄼ", "ㄽ", "ㄾ", "ㄿ", "ㅀ", "ㅁ", "ㅂ", "ㅄ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"] # 종성

# print(len(CHO))
# print(len(JUNG))
# print(len(JONG))

# print(chr(((0 * 21) + 0) * 28 + 0 + 44032)) # 가
# print(chr(((0 * 21) + 0) * 28 + 1 + 44032)) # 각

WORD_LIST = [
    # "Python programming",
    # "Let's coding~",
    # "Merry Christmas!"
    "파이썬 프로그래밍",
    "코딩하자~",
    "메리 크리스마스!"
]

random.shuffle(WORD_LIST)

def break_korean(string):
    word_list = list(string)
    break_word = []

    for k in word_list:
        if ord(k) >= ord("가") and ord(k) <= ord("힣"):
            # 유니코드상 몇 번째 글자인지 인덱스를 구합니다.
            char_index = ord(k) - ord("가")

            # 초성 = (유니코드 인덱스 / 28) / 21
            char1 = int((char_index / 28) / 21)
            break_word.append(CHO[char1])

            # 중성 = (유니코드 인텍스 / 28) % 21ㅔㅛ
            char2 = int((char_index / 28) % 21) 
            break_word.append(JUNG[char2])

            # 종성 = 유니코드 인텍스 % 28
            char3 = int(char_index % 28)
            if char3 > 0:
                break_word.append(JONG[char3])

        else:
            break_word.append(k)
    
    # print("input: {}".format(user_input)) 
    # print("break: {}".format(break_word))

    return break_word

for q in WORD_LIST:
    os.system("cls")
    start_time = time.time()
    user_input = str(input(q+'\n')).strip()
    end_time = time.time() - start_time

    src = break_korean(q)
    tar = break_korean(user_input)

    if user_input == "/exit":
        break

    correct = 0
    for i, c in enumerate(tar):
        if i >= len(src):
            break
        if c == src[i]:
            correct += 1
    
    tot_len = len(src)
    c = correct / tot_len * 100
    e = (tot_len - correct) / tot_len * 100
    speed = (correct / end_time) * 60

    print("speed : {:0.2f}, correct : {:0.2f}, typo : {:0.2f}".format(speed, c, e))
    os.system("pause")
