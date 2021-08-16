
def work(f, a, b, n):
    print("\nТекущее число разбиений: ", n)
    h = (b - a) / float(n)
    print("Текущий шаг:", h)
    total = sum([f((a + (k * h))) for k in range(0, n)])
    result = h * total
    print("Текущий результат: ", result)
    return result


def left_rectangles(function):
    """Запуск программы"""
    print("Используем формулу левых прямоугольников")

    """Задаем отрезок интегрирования"""
    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    h = float(input("Точность: "))
    max_step = int(input("Количество максимальных шагов: "))

    step = 0
    n = 2
    a1 = work(function, a, b, n)
    n *= 2
    a2 = work(function, a, b, n)

    while abs(a1 - a2) > h:
        n *= 2
        a1 = work(function, a, b, n)
        n *= 2
        a2 = work(function, a, b, n)
        step += 1
        if step >= max_step:
            print('Превышен лимит шагов')
            break

    print("\nОтвет:", a2, "\nКоличество разбиений:", n)


if __name__ == '__main__':
    left_rectangles()
