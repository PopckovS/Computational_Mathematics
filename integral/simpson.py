"""
Лабораторная работа №3
Численные методы вычисления определенных интегралов.
Методом Симпсона.

Интегрируемая функция: x / x^4 + 3X^2 + 2
Отрезок: [a,b]

H = (b-a) / n  где n-лич частей на которые разбиваем рисунок
y = f(x) площадь лежащая под кривой, между отрезками Xi и Xi+1
"""
import math


def finde_h(left, right, n):
    # return (right - left) / (2 * n)
    return (right - left) / n


def func(x):
    """Формула для расчета"""
    y = x / (pow(x, 4) + 3 * pow(x, 2) + 2)
    return y


def get_param():
    """Получаем данные от пользователя"""
    a = int(input('Введите левую границу a :'))
    b = int(input('Введите правую границу b :'))
    n = int(input('Введите личество разбиений n :'))
    return a, b, n


def table_calculations(a, n, h):
    """Генерация таблицы с вычислениями Xi Yi"""
    values = []
    result = a - h

    for i in range(n+1):
        result = result + h
        result = round(result, 1)
        values.append({result: func(result)})

    show_table(values)
    return values, list(values[len(values)-1].values())[0]


def show_table(values):
    """Показывает расчитанные значения X и Y"""
    print('='*28)
    print('  i  |  X    |    Y')
    print('=' * 28)
    for i in range(len(values)):
        for key, value in values[i].items():
            print(' {i}   |  {key}  |  {value}'.format(i=i, key=key, value=value))
    print('=' * 28)


def get_k(a, b, n, h):
    """Метод получаем сумму (четных/не четных) вычислений функции y = f(x)"""
    table_calcul, Yn = table_calculations(a, n, h)
    list_even, list_odd = [], []
    k_even, k_odd = 0, 0

    # Делим все полученные вычисленяи на 2 списка, с чет и нечет элементами
    for step in range(len(table_calcul)):
        if not (step == 0 or step == len(table_calcul)-1):
            if step % 2 == 0:
                list_even.append(list(table_calcul[step].values())[0])
            else:
                list_odd.append(list(table_calcul[step].values())[0])

    # Считаем сумму всех четных элементов
    for elem in list_even:
        k_even += elem

    # Считаем сумму всех не четных элементов
    for elem in list_odd:
        k_odd += elem

    print('(Y2+Y4...Yn-2) = ', list_even, ' = ', k_even)
    print('(Y1+Y3...Yn-1) = ', list_odd, ' = ', k_odd)

    return k_even, k_odd, Yn


def start():
    a, b, n = get_param()
    h = finde_h(a, b, n)
    print('h = ', h)
    k_even, k_odd, Yn = get_k(a, b, n, h)
    Y0 = func(a)

    # I = h/3 * ( Y0 + Yn + 4 * (Y1+Y3...Yn-1) + 2 * (Y2+Y4...Yn-2) )
    result = h/3 * ( Y0 + Yn + 4 * k_odd + 2 * k_even)
    print('По Формуле: h/3 * ( Y0 + Yn + 4 * (Y1+Y3...Yn-1) + 2 * (Y2+Y4...Yn-2) )')
    print('Подставляем: {h}/3 * {Y0} + {Yn} + 4 * {k_odd} + 2 * {k_even} = {result}'.
          format(h=h, Y0=Y0, Yn=Yn, k_odd=k_odd, k_even=k_even, result=result)
    )


start()






