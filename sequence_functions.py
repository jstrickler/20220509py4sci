
x = bytes([1, 2, 3, 4])
print("x: {}".format(x))

temp = "22\u00B0 C"
print("temp: {}".format(temp))

btemp = temp.encode()
print("btemp: {}".format(btemp))

t2 = btemp.decode()
print("t2: {}".format(t2))

colors = ['purple', 'pink', 'puce', 'blue', 'black']

print(len(colors), min(colors), max(colors), sorted(colors), '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]
print(len(nums), min(nums), max(nums), sorted(nums), sum(nums), '\n')

s = 'sequoia'
print(len(s), min(s), max(s), sorted(s), '\n')

print("colors: {}".format(colors))
rcolors = reversed(colors)
colors.append('yellow')
colors.insert(2, 'green')
print("colors: {}".format(colors))

print("rcolors: {}".format(rcolors))
for color in rcolors:
    print(color)
print('-' * 60)

r1 = reversed(colors)
print("list(r1): {}".format(list(r1)))
print("list(r1): {}".format(list(r1)))
print()

# for (i = 0; i < len(x); i++) {
#     printf("%s\n", thing[i])
# }

for i, color in enumerate(colors):
    print(i, color)
print('-' * 60)

print("list(enumerate(colors)): {}".format(list(enumerate(colors))))






