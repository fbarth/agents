import math
import random
import copy
import numpy as np
from Player import Player

class AutoPlayer(Player):

    def isPossibleMove(self, board, column):
        '''
        input: game board [matriz (6 x 7)]
        output: boolean
        description: check if the column is 
            not full and the column is 
            inside the board
        '''
        isFullColumn = board[0][column] != 0
        insideBoard = column < 7 and column >=0
        return insideBoard and not(isFullColumn)  
    
    def getOpponentCode(self, playerCode):
        '''
        input: player code [int]
        output: opponent code [int]
        description: creturn the opponent code [int]
        '''
        if playerCode == 1:
            return 2
        return 1

    def movement(self, player, board, column):
        result_board = np.matrix(board)
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board

    def sucessors(self, playerCode, board):
        '''
        input: player code [int], game board [matriz (6 x 7)]
        output: all possible sucessors states [list]
        description: checks all possible next states for
            the game, and return in a list
        '''
        suc = []
        for i in range(0,7):
            b = self.movement(playerCode, board, i)
            if(b is not None):
                suc.append({'board':b, 'action':i})
        return suc

    def calculateScore(self, x, y, board, playerCode):
        round_positions = [ 
        [-1, -1],[0, -1],[1, -1],
        [-1,  0],        [1,  0],
        [-1,  1],[0,  1],[1,  1]
        ]

        score = 0
        for pos in round_positions:
            new_x = x + pos[0]
            new_y = y + pos[1]
            if (new_x >= 0 and new_x <= 6) and (new_y >= 0 and new_y <= 5):
                if int(board[x][y]) == playerCode:
                    if int(board[new_y][new_x]) == playerCode:
                        score += 1
                    elif int(board[new_y][new_x]) == self.getOpponentCode(playerCode):
                        score -= 1
        return score

    def calculateHeapMap(self, playerCode, board):
        heat_map = np.zeros((6,7))
        board_list = copy.deepcopy(board).tolist()
        board_score = 0
        for row in range(len(board_list)):
            for column in range(len(board_list[row])):
                heat_map[row][column] = self.calculateScore(row, column, board_list, playerCode)
        for row in heat_map:
            board_score += sum(row)
        return board_score*10
    
    def countLinks(self, playerCode, board, typeLink):
        retorno = {"2": 0, "3": 0, "4": 0}
        if typeLink == "row":
            for i in range(6):
                counter = 0
                for j in range(6):
                    if ((board[i, j] == playerCode) and (board[i, j] == board[i, j + 1])):
                        counter = counter + 1
                    else:
                        counter = 0
                    if (counter==1):
                        retorno['2'] = retorno['2'] + 1
                    if (counter==2):
                        retorno['3'] = retorno['3'] + 1
                    if (counter==3):
                        retorno['4'] = retorno['4'] + 1
        elif typeLink == "column":
            for i in range(6):
                counter = 0
                for j in range(5):
                    if ((board[j, i] == playerCode) and (board[j,i] == board[j+1,i])):
                        counter = counter + 1
                    else:
                        counter = 0
                    if (counter==1):
                        retorno['2'] = retorno['2'] + 1
                    if (counter==2):
                        retorno['3'] = retorno['3'] + 1
                    if (counter==3):
                        retorno['4'] = retorno['4'] + 1
        else:
            for k in range(-2,4):
                counter = 0
                x = np.diag(board, k=k)
                for i in range(0,len(x)-1):
                    if ((x[i] == playerCode) and (x[i] == x[i+1])):
                        counter = counter + 1
                    else:
                        counter = 0
                    if (counter==1):
                        retorno['2'] = retorno['2'] + 1
                    if (counter==2):
                        retorno['3'] = retorno['3'] + 1
                    if (counter==3):
                        retorno['4'] = retorno['4'] + 1
        return retorno

    def agregateAllResults(self, countLinksObject):
        return countLinksObject["2"] + countLinksObject["3"]*10000 + countLinksObject["4"]*100000
    
    def eval(self, playerCode, board):
        oppCode = self.getOpponentCode(playerCode)
        heatMap = self.calculateHeapMap(playerCode, board)

        playerCounterRow = self.agregateAllResults(self.countLinks(playerCode, board, "row"))
        playerCounterCol = self.agregateAllResults(self.countLinks(playerCode, board, "column"))
        playerCounterDiag = self.agregateAllResults(self.countLinks(playerCode, board, "diag"))
        totalPlayer = playerCounterRow + playerCounterCol + playerCounterDiag

        opponentCounterRow = self.agregateAllResults(self.countLinks(oppCode, board, "row"))
        opponentCounterCol = self.agregateAllResults(self.countLinks(oppCode, board, "column"))
        opponentCounterDiag = self.agregateAllResults(self.countLinks(oppCode, board, "diag"))
        totalOpponent = opponentCounterRow + opponentCounterCol + opponentCounterDiag
        return totalPlayer - totalOpponent + heatMap

    def _max(self, board, move, alpha, beta, depth, playerCode):
        '''
        input:
        output:
        description:
        '''
        if depth == 0:
            return self.eval(playerCode, board), move
        for mv in self.sucessors(playerCode, board):
            new_alpha, new_move = self._min(mv["board"], mv["action"], alpha, beta, depth-1, playerCode)
            if (new_alpha > alpha):
                alpha = new_alpha
                move = new_move
            if (alpha >= beta):
                break
        return alpha, move
    
    def _min(self, board, move, alpha, beta, depth, playerCode):
        '''
        input:
        output:
        description:
        '''
        if depth == 0:
            return self.eval(playerCode, board), move
        for mv in self.sucessors(playerCode, board):
            new_beta, new_move = self._max(mv["board"], mv["action"], alpha, beta, depth-1, playerCode)
            if (new_beta < beta):
                beta = new_beta
                move = new_move
            if (beta <= alpha):
                break
        return beta, move
    
    def negamax(self, board, move, alpha, beta, depth, playerCode):
        if depth == 0:
            return self.eval(playerCode, board), move
        score = -9999999
        best_move = None
        for mv in self.sucessors(playerCode, board):
            new_score, new_action = self.negamax(mv["board"], mv["action"], -beta, -alpha, depth-1, playerCode)
            if (new_score > score):
                score = new_score
                best_move = new_action

            #pruning
            if score > alpha:
                alpha = score
            if alpha >= beta:
                break
        return score, best_move

    def findDiff(self, board1, board2):
        for i in range(len(board1)):
            for j in range(len(board1[i])):
                if board1[i][j] != board2[i][j]:
                    return j

    def simulateMovement(self, playerCode, column, board):
        copy_board = copy.deepcopy(board)
        for i in range(5,-2,-1):
            if (copy_board[i,column] == 0):
                break
        if self.isPossibleMove(copy_board, column):
            copy_board[i, column] = playerCode
        return copy_board

    def simulatePossibilities(self, playerCode, board):
        board_to_list = copy.deepcopy(board).tolist()
        for i in range(7):
            possibility = self.simulateMovement(playerCode, i, board)
            win = self.endOfGame(possibility)
            if win == True:
                possibility_to_list = copy.deepcopy(possibility).tolist()
                get_column = self.findDiff(board_to_list, possibility_to_list)
                return get_column
        return -1

    def endOfGame(self, board):
        for i in range(6):
            current = None
            counter = 0
            for j in range(6):
                if ((board[i, j] in (1,2)) and (board[i, j] == board[i, j + 1])):
                    if (board[i, j]==current):
                        counter = counter + 1
                        current = board[i, j]
                    else:
                        counter = 1
                        current = board[i, j]
                else:
                    counter = 0
                if (counter==3):
                    return True
        for i in range(7):
            current=None
            counter = 0
            for j in range(5):
                if ((board[j, i] in (1,2)) and (board[j,i] == board[j+1,i])):
                    if(board[j,i]==current):
                        counter = counter + 1
                        current = board[j,i]
                    else:
                        counter = 1
                        current = board[j,i]
                else:
                    counter = 0
                if (counter == 3):
                    return True
        for k in range(-2,4):
            current = None
            counter = 0
            x = np.diag(board, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] != 0) and (x[i] == x[i+1])):
                    if(x[i] == current):
                        counter = counter + 1
                        current = x[i]
                    else:
                        counter = 1
                        current = x[i]
                if (counter == 3):
                    return True
        temp = board[::-1]
        for k in range(-2,4):
            current = None
            counter = 0
            x = np.diag(temp, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] != 0) and (x[i] == x[i+1])):
                    if(x[i] == current):
                        counter = counter + 1
                        current = x[i]
                    else:
                        counter = 1
                        current = x[i]
                if (counter == 3):
                    return True

        return False

    #@Override
    def name(self):
        '''
        input: 
        output: string
        description: returns player name
        '''
        return "AutoPlayer"
    
    #@Override
    def move(self, playerCode, board):
        columnForWin = self.simulatePossibilities(playerCode, board)
        columnForOppWin = self.simulatePossibilities(self.getOpponentCode(playerCode), board)

        if columnForWin != -1:
            return None, columnForWin
        if columnForOppWin != -1:
            return None, columnForOppWin
        _, action = self.negamax(board, None, -9999999, 9999999, 9, playerCode)
        return None, action
        
