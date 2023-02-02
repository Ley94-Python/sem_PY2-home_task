n = int(input("Введите целое число: "))
k = 0
for i in range(1, n + 1):
    k = 2 * i
    if k >= n:
        break
    else:
        print(k)