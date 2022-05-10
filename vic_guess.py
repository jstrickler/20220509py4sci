import random

inp = input('Think of a number from 1 to 25... press any key to continue')
min =1
max = 25
answer = random.randint(min, max)
while inp.upper() != 'Y' :
    inp = input(f'Did you think of {answer}? Type "l" if low, "h" if high or "y" if correct: ')
    if inp.upper() == 'Y':
        break
    elif inp.upper() == 'L':
        min = answer+1
        answer = random.randint(min+1, 25)
    elif inp.upper() == 'H':
        max -= 1
        answer = random.randint(min, max)
    else:
        print('You can only enter l,h or y. Try again...')
