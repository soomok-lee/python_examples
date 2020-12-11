'''
08. 로또 번호 생성기 simple
'''
import random

count = int(input("how many? "))

for j in range(count):
    lotto = []  
    rand_num = random.randint(1, 46)

    for i in range(6):
        while rand_num in lotto:
            rand_num = random.randint(1, 46)
        lotto.append(rand_num)

    lotto.sort()
    print("{}. lotto: {}".format(j, lotto))

'''
09. 로또 번호 생성기 smart

1. 특정 숫자 포함
2. 특정 숫자 제외
3. 정해진 자리수만큼 연속 숫자를 포함
''' 
import numpy # pip install numpy

def make_lotto_number(**kwargs):
    rand_number = numpy.random.choice(range(1, 46), 6, replace=False)
    rand_number.sort()

    lotto = []

    # 1. 특정 숫자 포함
    if kwargs.get("include"):
        include = kwargs.get("include")
        lotto.extend(include)

        cnt_make = 6 - len(lotto)

        for _ in range(cnt_make): # _ instead of i
            for j in rand_number:
                if lotto.count (j) == 0:
                    lotto.append(j)
                    break
    else:
        lotto.extend(rand_number)
    
    # 2. 특정 숫자 제외
    if kwargs.get("exclude"):
        exclude = kwargs.get("exclude")
        lotto = list(set(lotto) - set(exclude))

        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1, 46), 6, replace=False)
                rand_number.sort()

                for j in rand_number:
                    if lotto.count(j) == 0 and j not in exclude:
                        lotto.append(j)
                        break


    #3. 정해진 자리수만큼 연속 숫자를 포함
    if kwargs.get("continuty"):
        continuty = kwargs.get("continuty")
        start_number = numpy.random.choice(lotto, 1)
        # print(start_number)

        seq_num = []
        for i in range(start_number[0], start_number[0] + continuty):
            seq_num.append(i)
        seq_num.sort()
        cnt_make = 6 - len(seq_num)
        lotto = []
        lotto.extend(seq_num)
        while len(lotto) != 6:
            for _ in range(6 - len(lotto)):
                rand_number = numpy.random.choice(range(1, 46), 6, replace=False)
                rand_number.sort()
            
            for j in rand_number:
                if lotto.count(j) == 0 and j not in seq_num:
                    lotto.append(j)
                    break
            
            lotto = list(set(lotto))

    lotto.sort()
    return lotto

print(make_lotto_number(include=[1, 2]))
print(make_lotto_number(exclude=[1, 2]))
print(make_lotto_number(continuty=2))


