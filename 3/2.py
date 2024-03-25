
try:
    a = int(input("Введите число "))
    b = 100 / a
    print(f"b = {b}")
except ZeroDivisionError:
    print('Ошибка! Деление на 0')

except ValueError:
    print('Ошибка! Деление на строку')