from pprint import pprint

file_path = "DATA/knights.txt"
knight_info = {}

with open(file_path) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = title, color, quest, comment

pprint(knight_info)
print('-' * 60)

# for key, value in DICT.items():
for knight, data in knight_info.items():
    print(data[0], knight)
print('-' * 60)


for dataset in knight_info.values():
    print(dataset)
print('-' * 60)
