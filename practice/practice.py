# # for
# a = [(1,2),(2,3),(3,4)]

# for i in a:
#     for j in i:
#         print(j)

# b = [[1,2,3,4,5], ['a','b','c'], [11,12,13,14]]

# for i in b:
#     for j in i:
#         print(j)

# c = [[[1,2,3,4,5], ['a','b','c'], [11,12,13,14]]]

# for i in c:
#     for j in i:
#         for k in j:
#             print(k)

# student = [{"ella":100},{"mari":200},{"john":300}]

# for i in student:
#     # print(type(i)) # dict
#     data = list(i.items())[0] # list
#     name = data[0]
#     value = data[1]
#     print("name : {}, score: {}".format(name, value))

# # enumerate
# for s, i in enumerate(student):
#     data = (list(i.items())[0])
#     name = data[0]
#     value = data[1]
#     print("{} name : {}, score: {}".format(s, name, value))

# msg = "python programming"

# for s, i in enumerate(msg, start=1):
#     print(s, i)

# result = []
# for num in range(1, 6):
#     result.append(num + 5)

# # one line for
# # comprehension
# result = [num + 5 for num in range(1,6)]
# print(result)

# result = [num + 5 for num in range(1,10) if num % 2 ==0]
# print(result)

# for num in range(1, 99):
#     if num % 2 == 0:
#         result.append(num * 3)

# result = [num * 3 for num in range(1,99) if num % 2 ==0]
# print(result)

# for i in range(2, 10):
#     for j in range(1, 10):
#         result = i * j
#         print("{} x {} = {}".format(i, j, i*j))
 
# gugudan = ["{} x {} = {}".format(i, j, i*j) for i in range(2, 10) for j in range(1, 10)]
# print(gugudan)

# # continue, break
# for i in range(1, 1000):
#     print(i)
#     if i == 10:
#         break
 
# num = 0
# while num < 10:
#     num += 1
#     if num == 5:
#         continue
#     print(num)

# hap = 0
# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     hap += i
# print("odds hap {}".format(hap))

# # input
# langs = ["korean", "english"]
# for i, l in enumerate(langs, start=1):
#     print("{}. {}".format(i, l))

# while True:
#     sel = input("choose a language.")

#     if not sel.isnumeric():
#         continue
        
#     sel = int(sel)
#     if 0 < sel < 3:
#         break
# print("your choice is {}.".format(langs[sel-1]))

# # range
# # range(stop)
# # range(start, stop)
# # range(start, stop, step)

# # prime number
# while True:
#     num = input("please input number above 2.")
#     if not num.isnumeric():
#         continue
    
#     num = int(num)
#     if num < 2:
#         continue
#     break

# prime_list = [False, False] + [True] * (num - 1) 
# primes = []

# for i in range(2, num + 1):
#     if prime_list[i]:
#         for j in range(2 * i, num + 1, i):
#             prime_list[j] = False

# primes = [i for i in range(2, num + 1) if prime_list[i] == True]
# print(primes)

# if num in primes:
#     print("isprime = true")
# else:
#     print("isprime = false")

# isprime = True
# for n in range(2, num):
#     if num % n == 0:
#         isprime = False
#         break

# if isprime:
#     print("isprime = true")

# else: 
#     print("isprime = false")

# # file
# file = open("sample.txt", mode="w", encoding="utf-8")
# file.write("hello world")
# file.close

# rfile = open("sample.txt", mode="r", encoding="utf-8") 
# content = rfile.readline()
# print(content)
# a = rfile.read(10) # read 10 characters
# print(a)
# rfile.close()

# with open("sample.txt", mode="r", encoding="utf-8") as file:
#     print(file.read())

# with open("sample1.txt", mode="r", encoding="utf-8") as file1, \ 
# open("sample2.txt", mode="w", encoding="utf-8") as file2: 
#     file2.write(file1.read())

# # try - except
# try:
#     idx = []
#     idx[0] = 100
# except Exception as e:
#     # print(e)
#     pass

# try:
#     # file = open("sample.txt", "r")
#     n = "10.5"
#     v = int(n)
# except:
#     print("error!")
# else:
#     print("good!")
# finally:
#     # file.close()
#     print("file closed.")

# # unicode, encoding
# a = "가"
# a.encode("utf-8")
# print(a) # cf) hexdump

# ord(a)
# bin(ord(a)) # binary

# file = open("utf8.txt", mode="rb")
# print(file.read().decode("utf-8")) # "가"
# file.close()

# file = open("utf8.txt", mode="r", encoding="utf-8")
# print(file.read()) # "가"
# file.close()

# # float
# float("10.1")
# print(0.1 + 0.2) # 0.30000000000000004
# print(0.1 + 0.2 == 0.3) # False

# import math
# math.isclose(0.1+0.2, 0.3)
# a = 0.1 + 0.2
# x,y = a.as_integer_ratio()
# print(a == x/y)

# a = "ella, mari"
# # a.split(",")
# # a.replace("ella", "coco")

# a = -1
# abs(a) # 1
# sum([1,2,3]) # 6

# all([True, True]) # True
# all([0, 1]) # False
# any([0, 1]) # True
# any([0, 0]) # False

# chr(97) # 'a'
# bin(10)
# oct(10)
# hex(10)

# a = 10
# isinstance(a, int) # True
# isinstance(a, str) # False

# # function 
def get_input_user(msg, casting=str):
    '''
    사용자에게 msg를 출력하고 casting 형태를 확인하여 입력된 값을 리턴합니다.

    Args:
        msg (str) : input 시 출력할 문구
        casting (class) : 사용자에게 입력 받은 값의 자료형

    Returns:
        user (casting-value) : 사용자에게 입력 받은 값
    '''
    while True:
        try:
            user = casting(input(msg))
            return user
        except:
            continue

user = get_input_user("input user name : ") # str
age = get_input_user("input user age : ", int)

print(user, age) 

def save_winner(*args): # args : keep the order
    print(args)

def save_winner2(**kwargs): # keyword args
    print(kwargs)
    if kwargs.get("name1"):
        print(kwargs["name1"])

save_winner("ella")
save_winner("ella", "mari")
save_winner2(name1 = "ella", name2 = "mari") 

def hi():
    print("hello")

hello = hi # hi()를 hello에 담아
hello()
print(type(hello)) # function

def add(a, b):
    print(a + b)
    return a + b

def cal(func, a, b):
    print("result {}".format(func(a, b)))

cal(add, 1, 5)

# function - function
def outer_function(func):
    def inner_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return inner_function

f = outer_function(add)
f(10, 20)

# module
import module
module.add(1, 4)