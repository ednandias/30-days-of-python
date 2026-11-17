"""
================================================================================

                                  LEVEL 1

================================================================================
"""

# 1. Iterate 0 to 10 using for loop, do the same using while loop.
c = 0
while c <= 10:
  print(c)
  c += 1

# 2. Iterate 10 to 0 using for loop, do the same using while loop.
c = 10
while c >= 0:
  print(c)
  c -= 1

# 3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
c = 1
hash = '#'
while c < 8:
  print(hash)
  hash += '#'
  c += 1

# 4. Use nested loops to create the following:
for i in range(1,8):
  print('# # # # # # # #')

  if i > 8:
    break

# 5. Print the following pattern:
for i in range(11):
  print('%s x %s = %s' % (i, i, i * i))

# 6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
for x in ['Python', 'Numpy','Pandas','Django', 'Flask']:
  print(x)

# 7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
  if i % 2 == 0:
    print(i)

# 8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
  if i % 2 != 0:
    print(i)


"""
================================================================================

                                  LEVEL 2

================================================================================
"""

# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
soma = 0
for i in range(101):
  soma = soma + i

print('The sum of all numbers is %s' % (soma))

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0
for i in range(101):
  if i % 2 == 0:
    even_sum = even_sum + i
  else:
    odd_sum = odd_sum + i

print('The sum of all evens is %s. And the sum of all odds is %s' % (even_sum, odd_sum))


"""
================================================================================

                                  LEVEL 3

================================================================================
"""

# 1. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

for country in countries:
  if country.find('land') != -1:
    print(country)

# 2. This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']

for i in range(len(fruits) - 1, -1, -1):
  print(fruits[i])

from countries_data import countries_data 

# 3. Go to the data folder and use the countries_data.py file. 

# i. What are the total number of languages in the data
languages = set()
for country in countries_data:
  for key, value in country.items():
    if (key == 'languages'):
      languages.update(value)

print(len(languages))

# ii. Find the ten most spoken languages from the data
most_spoken = dict()
for country in countries_data:
    for key, value in country.items():
        if (key == 'languages'):
          for language in value:
            if language in most_spoken:
              most_spoken[language] = most_spoken[language] + 1
            else:
              most_spoken[language] = 1      

def organize(key):
  return most_spoken.get(key)

spoken_sorted = sorted(most_spoken.keys(), key=organize, reverse=True)

print(spoken_sorted[:10])

# iii. Find the 10 most populated countries in the world
most_populated = dict()
for country in countries_data:
    for key, value in country.items():
      if key == 'population':
        most_populated[country['name']] = value

def organize(key):
  return most_populated.get(key)

populated_sorted = sorted(most_populated.keys(), key=organize, reverse=True)

print(populated_sorted[:10])

