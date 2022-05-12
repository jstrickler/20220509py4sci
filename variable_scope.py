
x = 100  # global (FILE-GLOBAL)

def spam():
    y = 42  # local (FUNCTION-LOCAL)
    print("in spam() x is", x)
    print("in spam() y is", y)

spam()
print("in main: x is", x)
# print("in main: y is", y)


