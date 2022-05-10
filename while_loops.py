
# while COND:
#    statement
#    statement

i = 0
while i < 3:
    print("i: {}".format(i))
    i += 1
print()

while True:
    user_name = input("Enter user name (q to quit): ")
    if user_name == 'q':
        break  # exit loop
    if user_name == '':
        print("Please enter a name...")
        continue  # go to top
    print(f"Welcome, {user_name}")


