'''
03. 영어 단어 맞추기 게임(random, for, if, dict)
'''
import random

words_dict = {
    "사자" : "lion",
    "호랑이" : "tiger",
    "사과" : "apple",
    "비행기" : "airplane"
}

words = []

for word in words_dict:
    words.append(word)

random.shuffle(words)

score = 0
chance = 3
for i in range(0, len(words)):
    q = words[i]
    for j in range(0, chance):
        user_input = str(input("input the word {} in english : ".format(q)))
        english = words_dict[q]

        if user_input.strip().lower() == english.lower():
            print("correct!")
            score += 1
            break
        else:
            print("wrong!")
        
    if user_input != english:
        print("the answer is '{}'.".format(english))
print("complete! your score is {}/{}".format(score, len(words)))