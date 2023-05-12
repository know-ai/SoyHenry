from random import shuffle

class Deck(list):
    r"""
    Documentation here
    """

    def __init__(self, size:int=20):

        self.size = size
        super(Deck, self).__init__(list(range(1, self.size+1)))

    @property
    def size(self)->int:

        return self._size

    @size.setter
    def size(self, value:int):
        r"""
        Documentation here
        """
        if isinstance(value, int):

            self._size = value

            if value < 1:

                self._size = None

                raise ValueError(f"Size {value} value must be greather than 0")

        else:

            self._size = None

            raise ValueError(f"Size {value} value must be an integer")
    
    def pop(self, pos:int=-1)->int:
        r"""
        Documentation here
        """
        if self.size > 0:
            
            value = super(Deck, self).pop(pos)
            self.size -= 1

            return value

    def shuffle(self)->None:
        r"""
        Documentation here
        """
        shuffle(self)

    def get_score(self, player_points:int, goal_score:int):
        r"""
        Documentation here
        """
        card = -1

        while player_points <= goal_score:

            player_points += self[card]

            card -= 1

        points = 10 + card + 1

        return points




