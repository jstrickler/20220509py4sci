from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck("Delilah")
print("d1: {}".format(d1))

# print(d1._dealer) # NAUGHTY

print("d1.dealer: {}".format(d1.dealer))  # NICE

d1.dealer = "Fred"

print("d1.dealer: {}".format(d1.dealer))

try:
    d1.dealer = 89.3
except TypeError as err:
    print(err)
else:
    print("d1.dealer: {}".format(d1.dealer))

d1.shuffle()

print("d1.cards: {}\n".format(d1.cards))

for _ in range(10):
    card = d1.draw()
    print("card: {}".format(card))
print('-' * 60)

j1 = JokerDeck("Jill")
j1.shuffle()
print(j1.dealer)
print("j1.cards: {}".format(j1.cards))

print(len(d1), len(j1))
print("j1: {}".format(j1))
print("d1: {}".format(d1))

