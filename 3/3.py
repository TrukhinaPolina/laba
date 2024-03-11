a = int(input("день "))
b = int(input("месяц "))
c = int(input("год "))
if 99 < c < 999:
    d = str(c)
    c = int(d[1:])
if 999 < c < 9999:
    d = str(c)
    c = int(d[2:])
result = a * b == c
print(result)