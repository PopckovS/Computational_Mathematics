"""
Программа Python для реализации метода Рунге-Кутта

Пример дифференциального уравнения:
dy / dx = 1+x^2+(2*x*y)/(1+x^2) и y(1)=3
"""


# Находит значение y для заданного x, используя размер шага h
# и начальное значение y0 при x0.
def work(x0, y0, x, h, function):
    """
    Подсчитать количество итераций, используя размер шага или
    высота шага h
    """

    n = (int)((x - x0) / h)

    # Итерировать по количеству итераций
    y = y0

    for i in range(1, n + 1):
        k1 = h * function(x0, y)
        k2 = h * function(x0 + 0.5 * h, y + 0.5 * k1)
        k3 = h * function(x0 + 0.5 * h, y + 0.5 * k2)
        k4 = h * function(x0 + h, y + k3)
        # Обновить следующее значение y
        y = y + (1.0 / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        # Обновить следующее значение x
        x0 = x0 + h
    return y


def runge_kutt(function):
    """Старт программы"""
    x0 = int(input('Введите x0: '))
    y = 3
    x = int(input('Введите x: '))
    h = float(input('Введите h: '))

    print(work(x0, y, x, h, function))


if __name__ == "__main__":
    runge_kutt()