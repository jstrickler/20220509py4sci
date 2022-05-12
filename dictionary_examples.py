from pprint import pprint

d1 = dict()  # empty dict
d2 = {'m': 19, 'r': 34, 'a': 81, 'z': 4}
d3 = {}

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

airports['AUS'] = 'Austin'
airports['JFK'] = 'NY-Kennedy'

pprint(airports, sort_dicts=False)
airports['JFK'] = "Kennedy"
print()
pprint(airports, sort_dicts=False)

print("airports['JFK']: {}".format(airports['JFK']))
print("airports['MCO']: {}".format(airports['MCO']))

# print("airports['LGA']: {}".format(airports['LGA']))

print("airports.get('LGA'): {}".format(airports.get('LGA')))
print("airports.get('LGA', 'NOT FOUND'): {}".format(airports.get('LGA', 'NOT FOUND')))

print()

pprint(airports)


print("airports.setdefault('LGA', 'La Guardia'): {}".format(airports.setdefault('LGA', 'La Guardia')))
pprint(airports, sort_dicts=False)
print()

for code in 'MCA', 'MCO', 'RDU', 'RDUX', "WOMBAT", 'OAK':
    print(code, code in airports)
print()


for code in airports:
    print(code)
print()

for code, name in airports.items():
    print(code, name)
print()

print("airports.items(): {}".format(airports.items()))
print()

for code, name in sorted(airports.items()):
    print(code, name)
print()
