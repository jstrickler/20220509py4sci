
cities = ['Arlington', 'Durham', 'Brooklyn',
          'Plano', 'Bastrop', 'Lake Woebegon',
          'San Francisco', 'Richmond', 'Pittsburgh', 'Arlington']

print("cities.count('Arlington'): {}".format(cities.count('Arlington')))
print("cities.count('Durham'): {}".format(cities.count('Durham')))
print("cities.count('Walnut Creek'): {}".format(cities.count('Walnut Creek')))

# for VAR ... in ITERABLE:
#    ...
#    ...
for city in cities:
    print(city)
print()

for city in sorted(cities):
    print(city)
print()

s = "abcd"
for char in s:  # equal to "foreach" in Perl, C#, etc
    # char = next(s)
    # char = next(s)
    # ...
    print(char)
print()

# iterables:
# str bytes tuple list dict dict.items() set generator

for city in cities[2:]:
    print(city)
print()

for city in cities[-5:]:
    print(city)
print()



