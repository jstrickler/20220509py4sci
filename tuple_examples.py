from dataclasses import dataclass
from datetime import date


# tuple like struct, but no name
# namedtuple  close to C struct
# >= 3.7  dataclasses  very much like a smart structure
# "normal" classes  structure on steroids do anything you want

@dataclass
class Person:
    first_name: str  #  type hints
    last_name: str
    product: str
    dob: date


person = ['Bill', 'Gates', 'Microsoft', '1955-10-28']  # list
person = {'Bill', 'Gates', 'Microsoft', '1955-10-28'}  # set
person = ('Bill', 'Gates', 'Microsoft', '1955-10-28')    # tuple
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'    # tuple

print(person[0], person[1])

first_name, last_name, product, dob = person # iterable unpacking
print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

print(people[0], type(people[0]), '\n')

for person in people:
    print(person[0], person[1])
print('-' * 60)

for first_name, last_name, _, _ in people:
    # var = next value of iterable
    # var, var, var, var = next value of iterable
    print(first_name, last_name)
print('-' * 60)

