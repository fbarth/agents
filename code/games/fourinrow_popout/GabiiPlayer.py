from Player import Player
import numpy as np
from random import randint
import copy

#
# authors: Fabricio Barth
# date: May, 2020

class GabiiPlayer(Player):

    def name(self):
        return "Gabii"

    def max_value(self, board, action, alpha, beta, player_code, p):
        if (p==0):
            return self.eval(player_code, board), action
        sucessores = self.sucessores(player_code, board)
        for s in sucessores:
            mv, ac = self.min_value(s['board'], s['action'], alpha, beta, player_code, p-1)
            if (mv > alpha):
                alpha = mv
                action = ac
            if (alpha >= beta):
                return alpha, action
        return alpha, action
    
    def min_value(self, board, action, alpha, beta, player_code, p):
        if (p==0):
            return self.eval(player_code, board), action
        sucessores = self.sucessores(player_code, board)
        for s in sucessores:
            mv, ac = self.max_value(s['board'], s['action'], alpha, beta, player_code, p-1)
            if (mv < beta):
                beta = mv
                action = ac
            if (beta <= alpha):
                return beta, action 
        return beta, action

    def diferente(self, board1, board2):
        for linha in range(len(board1)):
            for coluna in range(len(board1[linha])):
                if board1[linha][coluna] != board2[linha][coluna]:
                    return coluna

    def possibilidade(self,board,player_code):
        board_to_list = board.tolist()
        for i in range(7):
            possibility = self.movimentos(player_code, i, board)
            win = self.endOfGame(possibility)
            if win == True:
                possibility_to_list = copy.deepcopy(possibility).tolist()
                get_column = self.diferente(board_to_list, possibility_to_list)
                return get_column
        return -1

    def movimentos(self, playerCode, column, board):
        board_copia = copy.deepcopy(board)
        for i in range(5,-2,-1):
            if (board_copia[i,column] == 0):
                break
        if self.is_valid_location(board_copia, column):
            board_copia[i, column] = playerCode
        return board_copia

    def other_player(self,player_code):
        if(player_code == 1.0):
            other_code = 2.0
        else:
            other_code = 1.0
        return other_code

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

    def move(self, player_code, board):
        # se tem a possibilidade de ganahr
        col_ganha = self.possibilidade(board,player_code)
        if col_ganha != -1:
            return None,col_ganha

        #se tem possibilidade do outro jogador ganhar
        col_p_nao_perde= self.possibilidade(board,self.other_player(player_code))
        if col_p_nao_perde != -1:
            return None,col_p_nao_perde

        #se nao usa o mini_max_para definir
        _, action = self.max_value(board, None, -999999, 999999, player_code, 5)
       
        return None,action
        #return action
            

    def sucessores(self, player_code, board):
        suc = []
        for i in range(0,7):
            b = self.movement(player_code, board, i)
            if(b is not None):
                suc.append({'board':b, 'action':i})
        return suc

    def domain_center(self, player, board):
        h = np.matrix([
            [0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 0., 0., 0., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 1., 1., 1., 1., 1., 0.]])
        
        return np.sum(np.logical_and(board==player, h))

    def eval(self, player, board): 
        my_points_line = self.count_row_line(player, board)
        my_points_col = self.count_row_column(player, board)
        my_points_dig = self.count_row_diag(player, board)
        my_points_dig2 = self.count_row_diag(player, board[::-1])
        my_qtd_2 = my_points_line['2'] + my_points_col['2'] + my_points_dig['2'] + my_points_dig2['2']
        my_qtd_3 = my_points_line['3'] + my_points_col['3'] + my_points_dig['3'] + my_points_dig2['3']
        my_qtd_4 = my_points_line['4'] + my_points_col['4'] + my_points_dig['4'] + my_points_dig2['4']
        #print('my 2', str(my_qtd_2))
        #print('my 3', str(my_qtd_3))
        #print('my 4', str(my_qtd_4))
        sum_my_points = 100000*my_qtd_4 + 100*my_qtd_3 + my_qtd_2

        opponent = self.other_player(player)
        op_points_line = self.count_row_line(opponent, board)
        op_points_col = self.count_row_column(opponent, board)
        op_points_dig = self.count_row_diag(opponent, board)
        op_points_dig2 = self.count_row_diag(opponent, board[::-1])
        op_qtd_2 = op_points_line['2'] + op_points_col['2'] + op_points_dig['2'] + op_points_dig2['2']
        op_qtd_3 = op_points_line['3'] + op_points_col['3'] + op_points_dig['3'] + op_points_dig2['3']
        op_qtd_4 = op_points_line['4'] + op_points_col['4'] + op_points_dig['4'] + op_points_dig2['4']
        #print('op 2', str(op_qtd_2))
        #print('op 3', str(op_qtd_3))
        #print('op 4', str(op_qtd_4))
        sum_op_points = 100000*op_qtd_4 + 10000*op_qtd_3 + op_qtd_2
        
        return sum_my_points - sum_op_points + self.domain_center(player, board)

    def count_row_line(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        for i in range(6):
            counter = 0
            for j in range(6):
                if ((board[i, j] == player) and (board[i, j] == board[i, j + 1])):
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
    
    def count_row_column(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        for i in range(6):
            counter = 0
            for j in range(5):
                if ((board[j, i] == player) and (board[j,i] == board[j+1,i])):
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
    
    def count_row_diag(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        for k in range(-2,4):
            counter = 0
            x = np.diag(board, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] == player) and (x[i] == x[i+1])):
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
    def is_valid_location(bself,board, col):
        return board[0][col] == 0.0

    def movement(self, player, board, column):
        result_board = np.matrix(board)
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board