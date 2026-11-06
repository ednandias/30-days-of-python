from math import pi

def calculate_area(radius: float):
  return pi * (radius ** 2)

def calculate_circum(radius: float):
  return 2 * pi * radius

if (__name__ == "__main__"):
  area_of_circle = calculate_area(30)
  circum_of_circle = calculate_circum(30)

  print('Área do círculo:', area_of_circle)
  print('Circunferência do círculo:', circum_of_circle)

  user_radius = float(input('Digite o raio do círculo: '))

  print('Resultado:', calculate_area(user_radius))