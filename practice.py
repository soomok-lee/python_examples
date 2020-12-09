# for
a = [(1,2),(2,3),(3,4)]

for i in a:
    for j in i:
        print(j)

b = [[1,2,3,4,5], ['a','b','c'], [11,12,13,14]]

for i in b:
    for j in i:
        print(j)

c = [[[1,2,3,4,5], ['a','b','c'], [11,12,13,14]]]

for i in c:
    for j in i:
        for k in j:
            print(k)

student = [{"ella":100},{"mari":200},{"john":300}]

for i in student:
    # print(type(i)) # dict
    data = list(i.items())[0] # list
    name = data[0]
    value = data[1]
    print("name : {}, score: {}".format(name, value))

# enumerate
for s, i in enumerate(student):
    data = (list(i.items())[0])
    name = data[0]
    value = data[1]
    print("{} name : {}, score: {}".format(s, name, value))

msg = "python programming"

for s, i in enumerate(msg, start=1):
    print(s, i)

# result = []
# for num in range(1, 6):
#     result.append(num + 5)

# one line for
# comprehension
# result = [num + 5 for num in range(1,6)]
# print(result)

result = [num + 5 for num in range(1,10) if num % 2 ==0]
print(result)

# for num in range(1, 99):
#     if num % 2 == 0:
#         result.append(num * 3)

result = [num * 3 for num in range(1,99) if num % 2 ==0]
print(result)

# for i in range(2, 10):
#     for j in range(1, 10):
#         result = i * j
#         print("{} x {} = {}".format(i, j, i*j))
 
gugudan = ["{} x {} = {}".format(i, j, i*j) for i in range(2, 10) for j in range(1, 10)]
print(gugudan)

# continue, break
for i in range(1, 1000):
    print(i)
    if i == 10:
        break
 
num = 0
while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)

hap = 0
for i in range(1, 10):
    if i % 2 == 0:
        continue
    hap += i
print("odds hap {}".format(hap))

# input
langs = ["korean", "english"]
for i, l in enumerate(langs, start=1):
    print("{}. {}".format(i, l))

while True:
    sel = input("choose a language.")

    if not sel.isnumeric():
        continue
        
    sel = int(sel)
    if 0 < sel < 3:
        break
print("your choice is {}.".format(langs[sel-1]))

# range
# range(stop)
# range(start, stop)
# range(start, stop, step)

# prime number
while True:
    num = input("please input number above 2.")
    if not num.isnumeric():
        continue
    
    num = int(num)
    if num < 2:
        continue
    break

prime_list = [False, False] + [True] * (num - 1) 
# print(prime_list)
primes = []

for i in range(2, num + 1):
    if prime_list[i]:
        for j in range(2 * i, num + 1, i):
            prime_list[j] = False

primes = [i for i in range(2, num + 1) if prime_list[i] == True]
print(primes)

if num in primes:
    print("isprime = true")
else:
    print("isprime = false")

# isprime = True
# for n in range(2, num):
#     if num % n == 0:
#         isprime = False
#         break

# if isprime:
#     print("isprime = true")

# else: 
#     print("isprime = false")
