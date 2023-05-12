from .deck import Deck

class Player:
    r"""
    Documentation here
    """

    def __init__(self, cards:int=3):

        self.amount_of_cards = cards
        self.cards = list()

    def append_card(self, card:int):
        r"""
        Documentation here
        """
        if len(self.cards) < self.amount_of_cards:

            self.cards.append(card)

    def get_points(self):
        r"""
        Documentation here
        """
        return sum(self.cards)
    
class Crupier:
    r"""
    Documentation here
    """

    def __init__(self, deck_size:int):

        self.deck = Deck(size=deck_size)

    def shuffle(self):
        r"""
        Documentation here
        """
        self.deck.shuffle()

    def give_deck(self):
        r"""
        Documentation here
        """
        return self.deck.pop()