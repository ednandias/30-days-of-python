def calculate_rectangle(length: float, width: float):
  area = length * width
  perimeter = 2 * (length + width)

  return { 'area': area, 'perimeter': perimeter }

length = float(input('Length: '))
width = float(input('Width: '))

rec = calculate_rectangle(length, width)

print('Área:', rec.get('area'), '| Perímetro:', rec.get('perimeter'))