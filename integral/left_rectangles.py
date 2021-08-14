import math


def func(x):
    """Формула для расчета"""
    return math.pow(x,2)*math.pow(4-math.pow(x,2),-2)


def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b - a) / float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k * h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result


def start():
    """Запуск программы"""
    print("Используем формулу левых прямоугольников")
    print("Интегрируемая функция: f(x) = x^2*sqrt(4-x^2)")

    """Задаем отрезок интегрирования"""
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))

    n = 2
    a1 = work(func, a, b, n)
    n *= 2
    a2 = work(func, a, b, n)

    while abs(a1 - a2) > 0.001:
        n *= 2
        a1 = work(func, a, b, n)
        n *= 2
        a2 = work(func, a, b, n)

    print("\nОтвет:", a2, "\nКоличество разбиений:", n)
    input()


if __name__ == '__main__':
    start()
