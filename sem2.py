# Задача 1: Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# print('Введите вещественное число')
# n = input()
# s = 0
# while len(n) > 0:
#     d = n[-1]
#     if d.isdigit():
#         s += int(d)
#     n = n[:-1]
# print('Сумма:', s)

# Задача 2: Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n


print('Введите число')
n = int(input())
for i in range(1, n+1):
    print(fac(i))
