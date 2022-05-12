

cities = list()  # List cities = new List();
cities.append("Durham")
cities.append("Houston")
print("cities: {}".format(cities))
print("len(cities): {}".format(len(cities)))

class Animal:
    def run(self):
        print("Running!")

class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")

d = Dog()
d.bark()
d.run()

