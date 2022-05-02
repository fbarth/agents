
from Player import Player
import numpy as np
from random import randint

#
# authors: Fabricio Barth & Edgard Ortiz
# date: April, 2022

class MiniPlayer(Player):

    def name(self):
        return "Mini"

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

    def isThereAnyEmergency(self, board, player_code):
        opponent = self.opponent(player_code)
        op_points_line = self.count_row_line(opponent, board)
        op_points_col = self.count_row_column(opponent, board)
        op_points_dig = self.count_row_diag(opponent, board)
        op_points_dig2 = self.count_row_diag(opponent, board[::-1])
        if (op_points_col['3'] > 0 or op_points_line['3'] > 0 or op_points_dig['3'] > 0 or op_points_dig2['3']> 0):
            return True
        return False


    def move(self, player_code, board):
        _, action = self.max_value(board, None, -999999, 999999, player_code, 5)
        #print("Mini board ", board)
        n,availables= self.countBoard(board)
        if n < 5:
            if n < 4:
                if n < 3:
                    if board[5][3] != player_code:
                        return None,3
                if board[5][4] == 0:
                    return None,4
            if n > 3:
                if board[5][6] == 0:
                    return None,6
            if n < 3:
                if board[5][2] == 0:
                    return None,2
            else:
                pass
        if n > 41:
            for i in range(7):
                if board[5][i] == player_code:
                    return 'p',i
        AttackingCheckmate = self.checkCheckmate(True,player_code,board)
        if AttackingCheckmate[0]:
            #print("VIU ESSE ATAQUE?")
            return None,AttackingCheckmate[1]
        DefensiveCheckmate = self.checkCheckmate(False,player_code,board)
        if DefensiveCheckmate[0]:
            #print("TOMA ESSA DEFESA")
            return None,DefensiveCheckmate[1]
        #
        # Poderiamos fazer soh o
        #
        if (self.isThereAnyEmergency(board, player_code)):
            # simulando ser o adversario para identificar qual a jogada de vitoria
            sucessores = self.sucessores(self.opponent(player_code), board)
            for s in sucessores:
                v = self.eval(self.opponent(player_code), s['board'])
                if (v > 40000):
                    return None,s['action']

        if action is None:
            a = randint(0, len(availables)-1)
            action = availables[a]
        return None,action
            

        # sucessores = self.sucessores(player_code, board)
        # max_eval = 0
        # action = randint(3, 5)
        # for s in sucessores:
        #     v = self.eval(player_code, s['board'])
        #     print(str(s['action'])+' '+str(v))
        #     if (v > max_eval):
        #         max_eval = v
        #         action = s['action']
        # return action

    def sucessores(self, player_code, board):
        suc = []
        for i in range(0,7):
            b = self.movement(player_code, board, i)
            if(b is not None):
                suc.append({'board':b, 'action':i})
        return suc

    def opponent(self, player):
        if player==1:
            return 2
        return 1

    def domain_center(self, player, board):
        h = np.matrix([
            [0., 0., 0., 1., 0., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 0., 0.],
            [0., 0., 1., 1., 1., 1., 1.]])
        
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
        sum_my_points = 100000*my_qtd_4 + 10000*my_qtd_3 + my_qtd_2

        opponent = self.opponent(player)
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
        
        return sum_my_points - sum_op_points #+ self.domain_center(player, board)

    def count_row_line(self, player, board):
        retorno = {'2': 0, '3': 0, '4': 0}
        #max_counter = 0
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
        for i in range(7):
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

    
    def movement(self, player, board, column):
        result_board = np.matrix(board)
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board

    def checkCheckmate(self,attacking,player,board):
        if not(attacking):
            opponent = self.opponent(player)
        else:
            opponent = player
        threat = None
        #print("my opponent = ", opponent)
        for i in range(6):
            counter = 0
            for j in range(6):
                if ((board[i, j] == opponent) and (board[i, j+1] == opponent)):
                    counter = counter + 1
                    #print(f"counter = {counter}")
                else:
                    counter = 0
                if (counter >= 2):  # 3 mosqueteiros
                    if i == 5:  # Se estiver na última linha, não precisa checar linha de baixo
                        if j <= 3:
                            if board[i,j+2] == 0:
                                threat = j+2
                                return True, threat
                        if j >= 2:
                            if board[i,j-2] == 0:
                                threat = j-2
                                return True, threat
                    else:
                        #print(f"my counter row {i} col {j} = {counter}")
                        if j <= 3:
                            if (board[i,j+2] == 0) and (board[i+1,j+2] != 0):
                                threat = j+2
                                return True, threat
                        if j >= 2:
                            if board[i,j-2] == 0 and (board[i+1,j-2] != 0):
                                #print(f"my counter row {i} col {j} = {counter}")
                                threat = j-2
                                return True, threat

                if (counter >= 1):
                    #print(f"my counter row {i} col {j} = {counter}")
                    if i == 5:  # Se estiver na última linha, não precisa checar linha de baixo 
                        if j <= 3:
                            #print(f"Board[i,j+3] = {board[i, j+3]}")
                            if (board[i, j+3] == opponent) and (board[i,j+2] == 0):
                                threat = j+2
                                return True, threat 
                        if j >= 2:
                            #print(f"Board[i,j-2] = {board[i, j-2]}")
                            if (board[i,j-2] == opponent) and (board[i,j-1] == 0):
                                threat = j-1
                                return True, threat
                    else:
                        if j <= 3:
                            #print(f"Board[i,j+3] = {board[i, j+3]}")
                            if (board[i, j+3] == opponent) and (board[i,j+2] == 0) and (board[i+1,j+2] != 0):
                                threat = j+2
                                return True, threat 
                        if j >= 2:
                            #print(f"Board[i,j-2] = {board[i, j-2]}")
                            if (board[i,j-2] == opponent) and (board[i,j-1] == 0) and (board[i+1,j-1] != 0):
                                threat = j-1
                                return True, threat

        for i in reversed(range(7)):
            counter = 0
            for j in range(5):
                if ((board[j, i] == opponent) and (board[j+1,i] == opponent)):
                    counter = counter + 1
                else:
                    counter = 0
                if (counter >= 2):
                    if j >= 2:
                        #print(f"counter = {counter}")
                        #print(f"coluna= {i}")
                        #print(f"Board[j-1,i] = {board[j-1, i]}")
                        #print(f"Board[j-2,i] = {board[j-2, i]}")
                        if board[j-2,i] == 0:
                            #print("Ataque vertical coluna ",i)
                            threat = i
                            return True, threat
        #print("não achou nada")
        return False, threat

    def countBoard(self,board):
        s = 0
        availables = []
        for i in range(6):
            for j in range(7):
                if board[i,j] != 0:
                    s+=1
                else:
                    availables.append(j)
        return s,availables
