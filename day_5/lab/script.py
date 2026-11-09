""" 
================================================================================

                                  LEVEL 1

================================================================================
"""

# 1. Declare an empty list
empty = []

# 2. Declare a list with more than 5 items
five = [1,2,3,4,5]

# 3. Find the length of your list
print('3:',len(five))

# 4. Get the first item, the middle item and the last item of the list
print('4:',five[0],five[2],five[len(five) -1])

# 5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
info = ['Ednan', 24, '175cm', 'single', 'Rua Miguel Ruiz, 437']

# 6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7. Print the list using print()
print('7:',it_companies)

# 8. Print the number of companies in the list
print('8:',len(it_companies))

# 9. Print the first, middle and last company
print('9:',it_companies[0],it_companies[3],it_companies[len(it_companies) -1])

# 10. Print the list after modifying one of the companies
it_companies[4] = 'Mozilla'
print('10:',it_companies)

# 11. Add an IT company to it_companies
it_companies.append('Tesla')
print('11:',it_companies)

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(4, 'SpaceX')
print('12:',it_companies)

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print('13:',it_companies)

# 14. Join the it_companies with a string '#;  '
print('14:','#; '.join(it_companies))

# 15. Check if a certain company exists in the it_companies list.
print('15:','Amazon' in it_companies)

# 16. Sort the list using sort() method
it_companies.sort()
print('16:',it_companies)

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print('17:',it_companies)

# 18. Slice out the first 3 companies from the list
print('18:',it_companies[3:])

# 19. Slice out the last 3 companies from the list
print('19:',it_companies[:-3])

# 20. Slice out the middle IT company or companies from the list
del it_companies[:4]
print('20:',it_companies)

# 21. Remove the first IT company from the list
del it_companies[0]
print('21:', it_companies)

# 22. Remove the middle IT company or companies from the list
del it_companies[1]
print('22:', it_companies)

# 23. Remove the last IT company from the list
del it_companies[len(it_companies) -1]
print('23:', it_companies)

# 24. Remove all IT companies from the list
it_companies.clear()
print('24:', it_companies)

# 25. Remove all IT companies from the list
del it_companies

# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print('26:',full_stack)

# 27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print('27:', full_stack)

""" 
================================================================================

                                  LEVEL 2

================================================================================
"""

# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

"""
Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number )
Find the range of the ages (max minus min)
Compare the value of (min - average) and (max - average), use abs() method
"""

ages.sort()
maxAge = max(ages)
minAge = min(ages)
sumAges = sum(ages)
agesLen = len(ages)
average = sumAges / agesLen

one, two = ages[4:6]

print('max:', maxAge, 'min:',minAge)
print('median',(one + two) / 2)
print('average',average)
print('range',maxAge - minAge)
print('abs min',abs(minAge - average))
print('abs max',abs(maxAge - average))

# 2. Find the middle country(ies) in the countries list
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
];

typeNum = len(countries) % 2
countriesLen = len(countries)

middle = []

if (typeNum == 0):
  position = (countriesLen // 2 ) - 1
  middle = [countries[position], countries[position + 1]]
else:
  position = ((countriesLen + 1) // 2) -1
  middle = countries[position]

print('Middle Country(ies):',middle)

# 3. Divide the countries list into two equal lists if it is even if not one more country for the first half.

first = []
second = []

middle = (countriesLen + 1) // 2
first = countries[0:middle]
second = countries[middle:]

print('countries:',len(countries))
print('first:',len(first))
print('second:',len(second))

# 3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

china, russia, usa, *scandic = countries

print('scandic countries:',scandic)

