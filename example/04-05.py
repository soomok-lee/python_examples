'''
04. 콘솔 스마트 계산기 simple(calculator, list, for, eval)
10 + 20 * 10 = 210
'''
# import os

# while True:
#     os.system("cls")
#     s = input("input calculation formula : ")
#     print("result : {}".format(eval(s)))
#     os.system("pause")

'''
05. 콘솔 스마트 계산기 smart(calculator, list, for)
10 + 20 * 10 = 300
'''
import os

operator = ["+", "-", "*", "/", "="]

def string_calculator(user_input, show_hist=False):
    string_list = []
    lop = 0 # last_operator_position

    if user_input[-1] not in operator:
        user_input += "="
    for i, s in enumerate(user_input):
        if s in operator:
            if user_input[lop:i].strip() != "":
                string_list.append(user_input[lop:i].strip())
                string_list.append(s)
                lop = i + 1

    string_list = string_list[:-1] # - "="

    pos = 0
    while True:
        if pos + 1 > len(string_list):
            break
        if len(string_list) > pos + 1 and string_list[pos] in operator:
            temp = string_list[pos-1] + string_list[pos] + string_list[pos+1]
            del string_list[0:3]
            string_list.insert(0, str(eval(temp)))
            pos = 0

            if show_hist:
                print(string_list)
        pos += 1

    if len(string_list) > 0:
        result = float(string_list[0])

    return round(result, 4)

while True:
    os.system("cls")
    # user_input = "5 + 5 * 10"
    user_input = input("input calculation folmula : ")
    if user_input == "/exit":
        break
    result = string_calculator(user_input, show_hist=True)
    print("result : {}".format(result))
    os.system("pause")