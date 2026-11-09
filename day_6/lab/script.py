""" 
================================================================================

                                  LEVEL 1

================================================================================
"""

# 1. Create an empty tuple
tup = ()

# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
brothers = ('Danilo','Lucas', 'Vitor','Brenner')
sisters = ('Beatryz', 'Bianca', 'Gabriela')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append('Edimar')
family_members.append('Vera')
family_members = tuple(family_members)


""" 
================================================================================

                                  LEVEL 2

================================================================================
"""

# 1. Unpack siblings and parents from family_members
siblings = family_members[0:7]
parents = family_members[7:]
print(siblings)
print(parents)

# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Maça', 'Melancia', 'Banana', 'Uva')
vegetables = ('Alface', 'Brócolis', 'Repolho', 'Almeirão')
animal_products = ('Leite', 'Ovo', 'Costela', 'Frango')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3. Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = (len(food_stuff_lt) + 1) // 2
print(food_stuff_lt[0:middle])
print(food_stuff_lt[middle:])

# 5. Slice out the first three items and the last three items from food_stuff_lt list
first_1, first_2, first_3, *rest, last_1, last_2, last_3 = food_stuff_lt
print(first_1, first_2, first_3, last_1, last_2, last_3)

# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# 7. Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
