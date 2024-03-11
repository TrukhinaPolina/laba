n = int(input("кол-во слов "))
k = " "
for word in range(n):
    word = input("введите слово ")
    k = k + " " + word
    n = n - 1
print(k)
