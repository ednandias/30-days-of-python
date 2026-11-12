""" 
Slope = É a inclinação entre os dois pontos. 
Slope = variação vertical ÷ variação horizontal.
================================================================================

8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

Fórmula: [y = mx + b] -> [y = 2x -2]

Slope (m): 2 -> (slope é o m ao lado esquerdo do x) -> 2
Y-intercept: (0, -2) -> (zera o eixo X) -> [y = 2(0) - 2] -> [y = 0 - 2 = -2] 
X-intercept: (1, 0) -> (zera o eixo y) -> [0 = 2(1) - 2] -> [0 = 2 - 2 = 0]

outra forma/fórmula de achar o slope:
(2,2) | (6,10)
1, y1 | x2, y2

m = y2 - y1
    -------
    x2 - x1

m = 10 - 2
    -------
    6 - 2

m = 8 / 4 = 2

================================================================================
"""

from day_1.lab.script import euclidean_distance

distance = euclidean_distance([2,2], [6,10])

print('Distância Euclidiana:',distance)

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
y = (-3) ** 2 + 6 * (-3) + 9

print(y)
