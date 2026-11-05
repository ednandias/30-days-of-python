def calc_triangle_area(base: float, height: float):
  return 0.5 * base * height

base = float(input('Enter base: '))
height = float(input('Enter height: '))

area = calc_triangle_area(base, height)

print('The area of the triangle is', area)


