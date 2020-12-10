# decorator
'''
이미 작성된 코드에 새로운 기능을 추가하여 함수 기능을 확장시키는 개념

python에서 함수는 일급객체
클로저 사용
함수 내 함수를 정의할 수 있음
'''

# def outer_function(msg):
#     def inner_function():
#         return "inner_function received a message {}.".format(msg)
#     return inner_function

# c = outer_function("hello")
# print(dir(c))
# print(type(c.__closure__)) # tuple
# print(len(c.__closure__)) # 1
# print(dir(c.__closure__[0]))
# print(c.__closure__[0].cell_contents) # hello

import time

# def test():
#     start_time = time.time()
#     for i in range(5):
#         time.sleep(0.1)
#     end_time = time.time() - start_time
#     print("함수 동작 시간 : {}".format(end_time))

# test()

def time_checker(func):
    def inner_function(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("함수 {} 동작시간 {}".format(func.__name__, end_time - start_time))
        return result
    return inner_function

@time_checker
def test1():
    for i in range(5):
        time.sleep(0.1)

@time_checker
def test2():
    for i in range(3):
        time.sleep(0.1)

# test1()
# test2()

# functools
from functools import wraps
def login_required(func):
    @wraps(func) # **important**
    def inner_function(*args, **kwargs):
        if not kwargs.get("is_login"):
            print("login failed.")
            return "login required."
        return func(*args, **kwargs)
    return inner_function

@login_required
def login():
    '''login test'''
    print("hello")

login()
print(login.__name__)
print(login.__doc__)

def add_tag(new_args):
    def decorator(func):
        def wrapper(name):
            return "<{}><{}></{}>".format(new_args, func(name), new_args)
        return wrapper
    return decorator

@add_tag("html")
def test(msg):
    return "hello" + msg

print(test("ella"))