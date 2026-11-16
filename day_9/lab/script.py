""" 
================================================================================

                                  LEVEL 1

================================================================================
"""

# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user_age = input('Enter you age: ')
print('You are old enough to drive.') if int(user_age) >= 18 else print('You need %s more years to learn to drive.' % (18 - int(user_age)))

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 24
user_age = int(input('Enter you age: '))

if user_age == my_age:
  print('Hey, we have the same age!')
elif user_age > my_age:
  print('You are 1 year older than me.') if user_age - my_age == 1 else print('You are %s %s older than me.' % (user_age - my_age, 'years'))
else:
  print('You are 1 year newer than me.') if my_age - user_age == 1 else print('You are %s %s newer than me.' % (my_age - user_age, 'years'))

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a = int(input('Enter number one: '))
b = int(input('Enter number two: '))

if a > b:
  print('%s is greater than %s' % (a, b))
elif a < b:
  print('%s is smaller than %s' % (a, b))
else:
  print('%s is equal to %s' % (a,b))


"""
================================================================================

                                  LEVEL 2

================================================================================
""" 

# 1. Write a code which gives grade to students according to theirs scores:

score = int(input('Enter your score: '))

if score >= 0 and score <= 59:
  print('F')
elif score > 59 and score <= 69:
  print('D')
elif score > 69 and score <= 79:
  print('C')
elif score > 79 and score <= 89:
  print('B')
else: 
  print('A')

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
autumn = ['September', 'October', 'November']
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']

month = input('Enter the month: ')

if month in autumn:
  print('Autumn!')
elif month in winter:
  print('Winter!')
elif month in spring:
  print('Spring!')
elif month in summer:
  print('Summer!')
else:
  print('Invalid month!')

# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Digit a fruit: ')

if (fruit in fruits):
  print('That fruit already exist in the list')
else:
  fruits.append(fruit)
  print(fruits)

"""
================================================================================

                                  LEVEL 3

================================================================================
"""

# 1. Here we have a person dictionary. Feel free to modify it!
person={
  'first_name': 'Ednan',
  'last_name': 'Dias',
  'age': 24,
  'country': 'Brazil',
  'is_married': False,
  'skills': ['JavaScript', 'React', 'Node', 'PostgreSQL', 'Python'],
  'address': {
      'street': 'Rua Miguel Ruiz, 437',
      'zipcode': '15885031'
  }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
  print(person['skills'][2])

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person and 'Python' in person['skills']:
  print('Python' in person['skills'])

skills = set(person['skills'])

# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if len(skills.difference({'JavaScript', 'React'})) == 0:
  print('He is a front end developer')
elif len(skills.difference({'Node', 'Python', 'PostgreSQL'})) == 0:
  print('He is a backend developer')
elif {'React', 'Node', 'PostgreSQL'}.issubset(skills):
  print('He is a fullstack developer')
else:
  print('unknown title')

# If the person is not married and if he lives in Brazil, print the information in the following format:
if not person['is_married'] and person['country'] == 'Brazil':
  print('%s lives in %s. He is not married.' % (person['first_name'], person['country']))






