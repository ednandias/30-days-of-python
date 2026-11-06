def calc_triangle_perimeter(a: float, b: float, c: float):
  return a + b + c

a = float(input('Enter side a: '))
b = float(input('Enter side b: '))
c = float(input('Enter side c: '))

perimeter = calc_triangle_perimeter(a, b, c)

print('The perimeter of the triangle is', perimeter)


