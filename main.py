
# Ввод координат по парам и вывод их в строку по парам

# coord_list = []
# for i in range(3):
#     coords = input(f'Введите координаты {i+1} пару через пробел: ').split(' -')
#     coord_list.append(coords)
# print(coord_list)


# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от - N до N

# *Примеры: *
#
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# number = int(input('Введите число: '))
#
# my_list = []
#
# for i in range(-number, number + 1):
#     my_list.append(i)

# print(my_list)  # Вывод в строку в квадратных скобках
# print(*my_list) # Вывод без скобок

# for i in my_list:
#   print(i) # Вывод в столбик
#   print(i, end=', ') # Вывод в строку через запятую

# print(*my_list, sep=', ') # Вывод в строку через запятую, в конце без запятой

# Вывод через функцию

# number = int(input('Введите число: '))
#
# my_list = [1, 2, 3]
# a, b, c = 1, 2, 3
#
# def func(a, b, c):
#     print(a, b, c, sep=' следующее число ', end='конец строки')
#
# func(*my_list)



# 2. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# number = int(input('Введите число: '))
#
# if (number % 5 == 0 and number % 10 == 0 or number % 15 == 0) and number % 30 != 0:
#     print('Условие выполнено')
# else:
#     print('Условие не выполнено')


# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#
# Пример:
# Для N = 5: 1, -3, 9, -27, 81

# my_list = []
# n = int(input('Введите число: '))
# for i in range(n):
#     my_list.append((-3)**i)  # Любое число в 0 степени дает 1
# print(*my_list, sep=', ')



# 3. Для натурального n создать список,
# состоящий из элементов последовательности 3*n + 1.
#
#   *пример*
#
#   -Для n = 6: ['1: 4', '2:, 7', '3: 10', '4: 13', '5: 16', '6: 19']

# n = int(input('Введите число: '))
# my_list = []
# for i in range(1, n + 1):
# #    my_list.append(str(i) + ':' + str(3*i+1))
#     my_list.append(f'{i}: {3*i+1}')
# print(my_list)

# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# для домашки задачи 3:
# (случайный вывод числа)
# import random # Библиотека рандом
#
# #print(random.randint(0, 100))
#
# # или
#
# from random import randint as rnd # можно любое название вместо rnd

# print(rnd(0, 100))

# вывод случайного (рандомного списка)

# size = int(input('Введите размер списка: '))
#
# rnd_list = []
# for i in range(size):
#     rnd_list.append(rnd(0, 100))
#
# print(rnd_list)
# random.shuffle(rnd_list) # встроенный метод для перемешивания значений
# print(rnd_list)

