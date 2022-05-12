john_countries = ['Italy', 'Germany', 'Spain', 'Malta', 'Kuwait', 'Iraq', 'Austria', 'Cyprus', 'Canada']
dante_countries = ['Denmark', 'France', 'Spain', 'Kuwait', 'Canada', 'Mexico', 'Mexico', 'Mexico', 'Mexico']

john = set(john_countries)
dante = set(dante_countries)
print("john: {}\n".format(john))
print("dante: {}\n".format(dante))
dante.add('France')
dante.add('Burkina Faso')
dante.add('Tuvalu')
print("dante: {}\n".format(dante))

print("john & dante: {}".format(john & dante))  # intersection
print("john ^ dante: {}".format(john ^ dante))  # xor
print("john | dante: {}".format(john | dante))  # union
print("john - dante: {}".format(john - dante))  # john only
print("dante - john): {}".format(dante - john)) # dante only

a = 1, 2, 3
b = 4, 5, 6

c = 1, 2, 3
d = 9, 8, 7
e = 4, 1, 9

result_set1 = {a, b}
result_set2 = {c, d, e}
print("result_set1 & result_set2: {}".format(result_set1 & result_set2))

