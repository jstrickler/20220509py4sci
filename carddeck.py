"""
Provide an object representing a deck of cards, including a Card object for each card.

Usage:
deck = CardDeck("Dealer-Name")
"""
import random

class Card:
    """
    One deck of cards
    """
    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit

    @property
    def rank(self):
        """
        Rank of this card

        :return:
        """
        return self._rank

    @property
    def suit(self):
        """
        Suit of this card

        :return:
        """
        return self._suit

    def __str__(self):
        return f"{self.rank}-{self.suit}"

    def __repr__(self):
        # Card('2', 'Diamonds')
        return f"Card('{self.rank}', '{self.suit}')"


class CardDeck:   # inherits from object
    """
    One standard deck of 52 playing cards


    """
    CLUB = '\u2663'
    DIAMOND = '\u2662'
    HEART = '\u2661'
    SPADE = '\u2660'

    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


    def __init__(self, dealer):
        self.dealer = dealer
        self._make_deck()

    def _make_deck(self):
        self._cards = []
        for suit in self.CLUB, self.DIAMOND, self.HEART, self.SPADE:
            for rank in self.RANKS:
                card = Card(rank, suit)
                self._cards.append(card)


    def shuffle(self):
        """
        Randomize all cards

        :return: None
        """
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    @property
    def cards(self):
        return self._cards



    @property  # decorator
    def dealer(self):  # getter property
        return self._dealer.upper()


    @dealer.setter  # also a decorator
    def dealer(self, dealer): # setter prop
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a str")

    @property
    def spam(self):
        return self._spam

    @property
    def ham(self):
        return self._ham

    @ham.setter
    def ham(self, value):
        self._ham = value

    def __str__(self):
        #  CardDeck:Delilah,42
        my_name = type(self).__name__
        return f"{my_name}:{self.dealer},{len(self)}"

    def __len__(self): # "dunder length"
        return len(self._cards)
