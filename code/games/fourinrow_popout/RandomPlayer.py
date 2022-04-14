from random import randint
from Player import Player

class RandomPlayer(Player):

    def name(self):
        return "Random"

    def bottomDiscExist(self, player_code, board, column):
        if board[5][column] == player_code:
            return True
        return False

    def move(self, player_code, board):
        x = randint(0,13)
        if x < 7:
            return None, x
        else:
            p = x - 7
            if self.bottomDiscExist(player_code, board, p):
                return 'p', p
            else: 
                return None, randint(0, 6)


