# 1. Create an empty dictionary called dog
dog = dict()

# 2. Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Bruce'
dog['color'] = 'Marrow'
dog['breed'] = 'Salsicha'
dog['legs'] = True
dog['age'] = 7
print(dog)

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name'] = 'Ednan'
student['last_name'] = 'Dias'
student['gender'] = 'Male'
student['age'] = 24
student['marital_status'] = 'single'
student['skills'] = ['Javascript', 'Typescript', 'Python']
student['country'] = 'Brazil'
student['city'] = 'Novais'
student['address'] = 'Rua Miguel Ruiz'

# 4. Get the length of the student dictionary
print(len(student))

# 5. Get the value of skills and check the data type, it should be a list
print(student.get('skills'))
print(type(student.get('skills')))

# 6. Modify the skills values by adding one or two skills
student['skills'].append('Node')
student['skills'].append('React')
print(student.get('skills'))

# 7. Get the dictionary keys as a list
print(student.keys())

# 8. Get the dictionary values as a list
print(student.values())

# 9. Change the dictionary to a list of tuples using items() method
print(student.items())

# 10. Delete one of the items in the dictionary
student.pop('skills')
print(student)

# 11. Delete one of the dictionaries
del student

