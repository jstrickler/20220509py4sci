value = 37.382038023
person = "Aaron"
city = "Green Bay"

#  str(value) + ' ' + str(person) + ' ' + str(city) + '\n'
print(value, person, city)

print(value, person, city, sep='/')
print(value, person, city, sep='#')
print(value, person, city, sep='')
print(value, person, city, sep=' == ')
print()

print(value) # '\n'
print(person)
print(city)
print()


print(value, end=' ')
print(person, end='#')
print(city)
print()

print(person, "lives in", city)
print(f"{person} lives in {city}")  # python 3.6
print(f"2 + 2 = {2 + 2}")
print("{} lives in {}".format(person, city))  # python 3.0
print("%s lives in %s" % (person, city))  # python 2
print("2 + 2 = {}".format(2 + 2))

print("city: {}".format(city))
print(f"city: {city}")

x = f"city: {city}"

folder = "FOO"
folder2 = "BLAH"
filename = "bar.txt"

file_path = f"{folder}/{folder2}/{filename}"
print("file_path: {}".format(file_path))

import os
file_path = os.path.join(folder, folder2, filename)
print("file_path: {}".format(file_path))



