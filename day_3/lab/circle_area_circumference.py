from day_2.lab.script import calculate_area, calculate_circum

radius = float(input('Radius of circle: '))

area = calculate_area(radius)
circum = calculate_circum(radius)

print('Circle area:', area, '| Circle circumference:', circum)