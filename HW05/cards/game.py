from .player import Player, Crupier


class Game:
    r"""
    Documentation here
    """

    def __init__(self, goal_score:int=50, deck_size:int=20, card_to_player:int=3):

        self.goal_score = goal_score
        self.player = Player(cards=card_to_player)
        self.crupier = Crupier(deck_size=deck_size)
        self.rounds = card_to_player

    def final_resume(self):
        r"""
        Documentation here
        """
        player_points = self.player.get_points()
        
        if player_points > self.goal_score:
        
            return f"You lost: {player_points}"
        
        score = self.crupier.deck.get_score(player_points=player_points, goal_score=self.goal_score)

        return f"Congrats!!! your score is: {score}"

    def play(self):
        r"""
        Documentation here
        """
        self.crupier.deck.shuffle()
        for round in range(self.rounds):

            card = self.crupier.give_deck()
            self.player.append_card(card)

        print(self.final_resume())