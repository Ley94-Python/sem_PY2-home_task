n = int(input("Введите количество монет: "))
m_min = 0
for n in range(n):
    n = int(input())
    if n == 0:
        m_min += 1
print(f" Результат {m_min}")

