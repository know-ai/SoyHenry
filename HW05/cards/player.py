from .deck import Deck

class Player:

    def __init__(self, cards:int=3):

        self.amount_of_cards = cards
        self.cards = list()

    def append_card(self, card:int):

        if len(self.cards) < self.amount_of_cards:

            self.cards.append(card)

    def get_points(self):

        return sum(self.cards)
    
class Crupier:

    def __init__(self, deck_size:int):

        self.deck = Deck(size=deck_size)

    def shuffle(self):

        self.deck.shuffle()

    def give_deck(self):

        return self.deck.pop()