import random

b = random.randint(1,100000)
n = int(input("угадывай чорт "))

if b == n:
    print("правильно чорт")
else:
    print("неправильно чорт число было", b )