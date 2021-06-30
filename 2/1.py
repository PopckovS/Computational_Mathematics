"""
Лабораторная работа №2
Численные методы решения дифференциальных уравнений.
Метод Эйлера.

Задается отрезок [a, b] и шаг h
Выходные данные: значения функции y в каждой из точек a, a+h, 2h,…, b
Уравнение:   y'=x^2-y/2x
Нач.условия: y(1)=1
"""
import math


def get_param():
    """
    Получаем отрезки и шаг от пользователя, и вычисляем
    количество шагов на отрезке с заданным шагом.
    """
    a = int(input('Введите начало отрезка a : '))
    b = int(input('Введите конец отрезка b : '))
    h = float(input('Введите шаг h : '))

    n = (b - a) / h
    return a, b, h, n


def func(x, y):
    """Вычисляем функцию"""
    return pow(x, 2) - y / 2 * x


def show_table(x_list: list, y_list: list):
    """Красивый вывод итоговых вычислений."""
    counter = 0
    print('  Итоговая таблица значений  ')
    print('----------------------------------')
    print(' X            |            Y      ')
    print('----------------------------------')
    while counter < len(x_list):
        print(x_list[counter],'          |   ', y_list[counter])
        counter += 1


def start():
    """Старт программы"""
    a, b, h, n = get_param()
    counter = 0
    # y = list(map(int,input('Введите чальные значения для Y')))
    # print('y = ', y)
    x_list = []
    y_list = [0, 1]

    while counter <= n:
        # Вычисляем новое значение для X
        x_list.append(round(a + counter * h, 1))
        # Вычисляем новое значение для Y
        y_list.append(y_list[counter-1] + h ** func(x_list[counter], y_list[counter-1]))
        counter += 1

    show_table(x_list, y_list)


start()














#
# import numpy as np
# # from matplotlib import pyplot as plt
# # import pylab
#
# def f(x):
#
#     return (math.e)**(-10*x)
#
# def euler(x):
#
#     y_init = 1
#     x_init = 0
#
#     old_dy_dx = -10*y_init
#
#     old_y = y_init
#
#     new_y = None
#
#     new_dy_dx = None
#
#     delta_x = 0.001
#
#     limite = 0
#
#     while x>limite:
#
#         #for i in range(1,6):
#
#         new_y = delta_x*old_dy_dx + old_y
#         #print ("new_y", new_y)
#
#         new_dy_dx = -10*new_y
#         #print ("new dy_dx", new_dy_dx)
#
#         old_y = new_y
#         #print ("old_y", old_y)
#
#         old_dy_dx = new_dy_dx
#         #print ("old delta y_delta x", old_dy_dx)
#         #print ("iterada",i)
#
#         limite = limite +delta_x
#
#     return new_y
#
# t = np.linspace(-1,5, 80)
#
# lista_outputs = []
#
# for i in t:
#     lista_outputs.append(euler(i))
#     print (i)
#
# # red dashes, blue squares and green triangles
# # plt.plot(t, f(t), 'b-', label='Output resultado analítico')
# # plt.plot(t , lista_outputs, 'ro', label="Output resultado numérico")
# # plt.title('Comparação Euler/Analítico - tolerância: 0.3')
# # pylab.legend(loc='upper left')
# # plt.show()
















