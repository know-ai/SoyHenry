from cards import Game

if __name__=="__main__":

    play = True

    while play:

        # Initial inputs
        goal_score = int(input("Goal Score (int): "))
        deck_size = int(input("Deck size (int): "))
        card_to_player = int(input("Number of card for player (int): "))

        # Game instantiation
        game = Game(
            goal_score=goal_score, 
            deck_size=deck_size, 
            card_to_player=card_to_player
        )
        # Play game
        game.play()

        # Ask for play gain
        play = input("Do you play again? (y/n): ")

        if play.lower() in ['yes', 'y', 'si']:

            play = True
        
        else:

            play = False