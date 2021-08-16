from .root.simple_iteration import simple_iteration
from .root.half_division import half_division
from .differential.euler import euler
from .differential.runge_kutt import runge_kutt
from .integral.simpson import simpson
from .integral.left_rectangles import left_rectangles

# Все модули для импортирования пакета
__all__ = [
    "NAME",
    "simple_iteration", "half_division",
    "euler", "runge_kutt",
    "simpson", "left_rectangles",
    ]

# Название пакета
NAME = 'ComputMath'
