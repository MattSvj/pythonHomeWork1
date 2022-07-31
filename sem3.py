# задача 1: Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# f = 0
# list_of_strings = ['qwe3f', 'vdf', 'wer', 'qwe']
# for string in list_of_strings:
#     for i in string:
#         if i.isdigit():
#             f = 1
# if f == 1:
#     print('Есть число')
# else:
#     print('Числа нет')

# Задача 2: Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list_of_strings = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
s = 0
q = list_of_strings[0]
for i in range(len(list_of_strings)):
    if q in list_of_strings[i]:
        ind = i
        s += 1
    if s == 2:
        print(ind)
        break