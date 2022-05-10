
list1 = list()
list2 = ['a', 'b', 'c']
list3 = []

cities = ['Arlington', 'Durham', 'Brooklyn',
          'Plano', 'Bastrop', 'Lake Woebegon',
          'San Francisco', 'Richmond', 'Pittsburgh']

print("cities: {}".format(cities))
print("len(cities): {}".format(len(cities)))

cities.insert(0, 'Houston')
cities.insert(4, 'Miami')

print("cities: {}".format(cities))

cities.append('Toronto')
cities.append('Calgary')
cities.append('Vancouver')

print("cities: {}".format(cities))

english_cities = ['Dover', 'London', 'Manchester', 'Nottingham']

cities.extend(english_cities)

print("cities: {}".format(cities))

#  LIST.insert(pos, value)   LIST.append(value)  LIST.extend(iterable)

cities.extend("Vik")
print("cities: {}".format(cities))

del cities[7]
print("cities: {}".format(cities))

cities.remove('Dover')  # raise error if 'Dover' not in list
print("cities: {}".format(cities))

print("'Plano' in cities: {}".format('Plano' in cities))
print("'Poughkeepsie' in cities: {}".format('Poughkeepsie' in cities))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

print("sorted(cities)): {}".format(sorted(cities)))

city = cities.pop()
print("city: {}".format(city))
print("cities: {}".format(cities))

city = cities.pop(3)
print("city: {}".format(city))
print("cities: {}".format(cities))
print("len(cities): {}".format(len(cities)))
cities.pop()
print("cities: {}".format(cities))

print("cities[0]: {}".format(cities[0]))
print("cities[5]: {}".format(cities[5]))
print("cities[14]: {}".format(cities[14]))
print("cities[-1]: {}".format(cities[-1]))
print("cities[len(cities)-1]: {}".format(cities[len(cities)-1]))
print("cities[-5]: {}".format(cities[-5]))

print("cities[0:5]: {}".format(cities[0:5]))
print("cities[4:7]: {}".format(cities[4:7]))

actor = "Chris Hemsworth"
print("actor: {}".format(actor))
print("actor[:5]: {}".format(actor[:5]))
print("actor[6:9]: {}".format(actor[6:9]))
print("actor[-5:]: {}".format(actor[-5:]))

print("cities[-5:]: {}".format(cities[-5:]))













