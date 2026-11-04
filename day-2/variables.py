# Day 2: 30 Days of Python programming

first_name = 'Ednan'
last_name = 'Dias'
full_name = 'Ednan Dias'
country = 'Brazil'
city = 'Novais'
age = 24
year = 2026
is_married = False
is_true = True
is_light_on = True

play_1, play_2, play_3, play_4, play_5 = True, True, False, False, True

print(play_1, play_2, play_3, play_4, play_5)

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))
print(len(first_name) == len(last_name))

num_one, num_two = 5,4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_two ** num_one
floor_division = num_one // num_two

print('Total:',total)
print('Diff:',diff)
print('Product:',product)
print('Division:',division)
print('Remainder:',remainder)
print('Exp:',exp)
print('Floor Division:',floor_division)

user_first_name = input('Nome: ')
user_last_name = input('Sobrenome: ')
user_country = input('País: ')
user_age = input('Idade: ')

print(user_first_name, user_last_name, user_country, user_age)

print(help('keywords'))