from carddeck import Card, CardDeck

class JokerDeck(CardDeck):

    def _make_deck(self):
        super()._make_deck() # call parent
        for rank in '1', '2':
            joker = Card(rank, '** JOKER **')
            self._cards.append(joker)
