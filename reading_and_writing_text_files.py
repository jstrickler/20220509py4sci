
file_path = 'DATA/mary.txt'
mary_in = open(file_path, 'r')
#  read file here and process the data
mary_in.close()

with open(file_path) as mary_in: # mary_in = open(...)
    pass

# read line-by-line
with open(file_path) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n
        print(line)
print('-' * 60)

# read file into single string
with open(file_path) as mary_in:
    contents = mary_in.read()
    print("raw contents:\n{}".format(repr(contents)), '\n')
    print("normal contents:\n{}".format(contents))
print('-' * 60)

# read into list of strings WITH newlines
with open(file_path) as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print("all_lines_with_nl:\n{}".format(all_lines_with_nl))
print('-' * 60)

# read into list of strings WITHOUT newlines
with open(file_path) as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print("all_lines_without_nl:\n{}".format(all_lines_without_nl))
print()

target = 'lizard'
count = 0

file_path = 'DATA/alice.txt'
output_path = f'{target}_lines.txt'
with open(file_path) as alice_in:
    with open(output_path, 'w') as alice_out:
        for line in alice_in:
            if target in line.lower():
                count += 1
                print(line.rstrip())
                alice_out.write(line)
print(f"{count} lines contain '{target}'\n")

file_path = 'DATA/knights.txt'
with open(file_path) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        print(title, name)
print()

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('capfruits.txt', 'w') as capfruits_out:
    for fruit in sorted(fruits):
        capfruits_out.write(fruit.capitalize() + '\n')

