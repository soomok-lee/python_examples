'''
01. 숫자 맞추기 게임(random, for, if)
'''
import random
import os

def input_check(msg, casting=int):
    while True:
        try:
            user_input = casting(input("number? "))
            return user_input
        except:
            continue

chance = 10
count = 0

number = random.randint(1, 99)
os.system("cls")
print("guess number between 1 and 99 in 10 times.")

while count < chance:
    count +=1
    user_input = input_check("number? ")
    if number == user_input:
        print("correct!")
        break
    elif user_input < number:
        print("bigger than {}".format(user_input))
    elif user_input > number:
        print("smaller than {}".format(user_input))
    
if user_input == number:
    print("success! {} is correct!".format(number))
else:
    print("fail! the answer is {}.".format(number))