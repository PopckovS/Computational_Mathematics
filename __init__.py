from .root import half_division, simple_iteration
from .differential import euler, runge_kutt
from .integral import left_rectangles, simpson

# Все модули для импортирования пакета
__all__ = [
    "NAME",
    "half_division",
    "simple_iteration",
    "euler",
    "runge_kutt",
    "simpson",
    "left_rectangles"
    ]

# Название пакета
NAME = 'ComputMath'
