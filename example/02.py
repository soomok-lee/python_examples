
'''
02. 숫자 야구 게임(random, for, if)
'''
import random
import os

numbers = []
number = str(random.randint(0, 9))
for i in range(3):
        while number in numbers:
            number = str(random.randint(0, 9))
        numbers.append(number)

os.system("cls")
print("*"*60)
print("-- game start --")
while True:
    count_strike = 0    
    count_ball = 0
    
    nums = str(input("input 3 digits : "))

    if len(nums) == 3 & len(set(nums)) == 3: # check length and duplication
        for i in range(0, 3):
            for j in range(0, 3):
                if nums[i] == numbers[j] and i == j:
                    count_strike += 1
                elif nums[i] == numbers[j] and i != j:
                    count_ball += 1

        if count_strike == 3:
            break
        elif count_strike == 0 and count_ball == 0:
            print("three out!")
        else:
            output = ""
            if count_strike > 0:
                output += "{} strike ".format(count_strike)
            if count_ball > 0:
                output += "{} ball ".format(count_ball)
            
            print(output)
print("success!")
print("-- game start --")
print("*"*60)