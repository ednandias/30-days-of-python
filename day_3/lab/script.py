print('python and dragon are the same length?',len('python') != len('dragon'))
print('is there on in python and dragon?','on' in 'python' and 'on' in 'dragon')
print('is jargon present in I hope this course is not full of jargon?','jargon' in 'I hope this course is not full of jargon')
print('is there any on in dragon and python?', not 'on' in 'python' and not 'on' in 'dragon')
print(str(float(len('python'))))
print(2 % 2 == 0)
print(5 % 2 == 0)
print(7 // 3 == int(2.7))
print('10' == 10)
print(float('9.8') == 10)

hours = input('Enter hours: ')
rate = input('Enter rate per hour: ')
print('Your weekly earning is', int(hours) * int(rate))

years_lived = input('Enter number of years you have lived: ')
print('You have lived for', int(years_lived) * 60 * 60 * 24 * 365)

print("""
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""
)



