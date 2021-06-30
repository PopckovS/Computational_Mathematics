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

    x_list = [1]
    y_list = [1]

    while counter <= n:
        # Вычисляем новое значение для X
        x_list.append(round(a + counter * h, 1))
        # Вычисляем новое значение для Y
        y_list.append(y_list[counter-1] + h * func(x_list[counter-1], y_list[counter-1]))
        counter += 1

    show_table(x_list, y_list)


start()






