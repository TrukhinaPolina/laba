a = int(input(""))
try:
    b = 100/a
except ZeroDivisionError:
    print('Ошибка! Деление на 0')
except ValueError:
    print('Ошибка! Деление на строку')
print(b)