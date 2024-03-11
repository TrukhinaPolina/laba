import random

n = 0
k = 0
while n < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    print(a, '+', b)
    c = int(input("= "))
    if (a + b) == c:
        print("Правильно! ")
        k = k + 1
    else:
        n = n + 1
        print("Ответ неверный ")
print("Игра окончена. Правильных ответов: ", k)