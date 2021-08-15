"""
Используем метод простой итерации для нахождения корней уравнения.
"""


# Для работы в терминале
def interactive_check_e(x_list, result, step, E):
    """Проверка рузультата на достижение точности E(кси)"""
    if abs(result - x_list[step]) < E:
        print('Точность перешла порог E (кси)')
        print('По формуле: |Xn+1 - Xn|')
        print('|{next} - {prev}| = {result} <= {E}'.format(
                    next=result,
                    prev=x_list[step],
                    result=abs(result - x_list[step]),
                    E=E
                )
        )
        return True


# Для работы в терминале
def interactive_show_step(step, current_x, result):
    """Показать информацию о текущем шаге"""
    print(f'Шаг №{step} при X{step} = {current_x} По формуле '
          f'(2 * math.cos({current_x})) / 7 = {result}'.
          format(step=step, result=result, current_x=current_x)
          )


# Для работы в терминале
def interactive_get_param():
    # Получаем данные от пользователя
    x0 = float(input('Введите X0 : '))
    E = float(input('Введите точность E(кси): '))
    x_list = [x0]
    max_step = 100
    return x0, E, x_list, max_step


# Для работы в терминале
def interactive_simple_iteration(function):
    """
    Цикл вычислений и проверок
    """
    x0, E, x_list, max_step = interactive_get_param()

    for step in range(max_step):
        current_x = x_list[step]
        result = function(current_x)
        interactive_show_step(step, current_x, result)
        x_list.append(result)
        if len(x_list) > 1 and interactive_check_e(x_list, result=result, step=step, E=E):
            break
    else:
        print('Метод простой итерации не сошелся')


# Не для интерактивной работы
def simple_iteration(x0, E, function, max_step=100):
    """
    Цикл вычислений и проверок
    """

    x_list = [x0]

    for step in range(max_step):
        x = x_list[step]
        # result = eval(function_expression)
        result = function(x)
        x_list.append(result)
        if len(x_list) > 1 and abs(result - x_list[step]) < E:
            return {'msg': 'OK',
                    'Результат': result - x_list[step],
                    'Все шаги': x_list,
                    'E(кси)': E,
                    'Количество шагов': step + 1
                    }
    else:
        return {'msg': 'Метод простой итерации не сошелся'}


# Запуск программы
if __name__ == "__main__":
    interactive_simple_iteration()
