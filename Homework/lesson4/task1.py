# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

import math
from math import pi

d =  len(input("Введите число d с заданной точностью:\n").split(".")[1])
print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')