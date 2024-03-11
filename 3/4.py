a = int(input())
if a % 2 == 0:
    n = len(str(a)) // 2
    c = str(a)[:n]
    b = str(a)[n:]
    x = int(c) // 100 + (int(c) // 10) % 10 + int(c) % 10
    y = int(b) // 100 + (int(b) // 10) % 10 + int(b) % 10
    if x == y:
        print("счастливый билетик")
    else:
        print("не счастливый билетик")

else:
    print('не четный ')
