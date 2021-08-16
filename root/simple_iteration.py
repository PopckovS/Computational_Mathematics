"""
Используем метод простой итерации для нахождения корней уравнения.

Пример уравнения:
           f(x) = 2 cos x -7x = 0; при  = 0.01
           f(x) = 7x = 2 cos x
           f(x) = x = (2 cos x) / 7
    Пусть x0 = 1 тогда:
    x1 = (2 cos x0) / 7
    x2 = (2 cos x1) / 7
    x3 = (2 cos x2) / 7
И так далее ... до тех пор пока |Xn+1 - Xn| <= E
"""
import math


def func(x):
    """Функция для вычислений"""
    return (2 * math.cos(x)) / 7


def check_e(result, step, E):
    """Проверка рузультата на достижение точности E(кси)"""
    if abs(result - x_list[step]) < E:
        print('Точность перешла порог E (кси)')
        print('По формуле: |Xn+1 - Xn|')
        print('|{next} - {prev}| = {result} <= {E}'.
            format(next=result, prev=x_list[step], result=abs(result - x_list[step - 1]), E=E)
        )
        return True


def show_step(step, current_x, result):
    """Показать информацию о текущем шаге"""
    print(f'Шаг №{step} при X{step} = {current_x} По формуле '
          f'(2 * math.cos({current_x})) / 7 = {result}'.
          format(step=step, result=result, current_x=current_x)
          )


def start():
    """
    Цикл вычислений и проверок
    """
    for step in range(max_step):
        current_x = x_list[step]
        result = func(current_x)
        show_step(step, current_x, result)
        x_list.append(result)
        if len(x_list) > 1 and check_e(result=result, step=step, E=E):
            break
    else:
        print('Метод простой итерации не сошелся')


# Получаем данные от пользователя
x0 = float(input('Введите X0 : '))
E = float(input('Введите точночть E(кси): '))
x_list = [x0]
max_step = 100

# Точка запуска программыы
start()





























































