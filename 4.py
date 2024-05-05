"""
1 - красный, 2 - синий, 3 - желтый

"""
import random

a = random.randint(1, 3)
b = random.randint(1, 3)
if a != b:
    if a + b == 3:
        print("фиолетовый")
    if a + b == 4:
        print("оранжевый")
    if a + b == 5:
        print("зеленый")
else:
    print("ошибка")
print(a)
print(b)
