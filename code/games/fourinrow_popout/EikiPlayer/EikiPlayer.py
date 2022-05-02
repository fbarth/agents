from Player import Player
import numpy as np
from keras.models import load_model
import pickle

x_global = []
y_global = []

class EikiPlayer(Player):

    classifier = load_model("./EikiPlayer/cnn_four_in_row.model")

    def transform_shape(self, board):
        tmp = np.asarray([[[0,0,0]]*7]*6)
        for i in range(board.shape[0]):
            for j in range(board.shape[1]):
                if board[i][j] == 1:
                    tmp[i][j] = [0,0,255]
                elif board[i][j] == 2:
                    tmp[i][j] = [0,255,0]
                else:
                    tmp[i][j] = [0,0,0]
        return np.asarray([tmp])

    def x(self):
        return x_global

    def y(self):
        return y_global

    def name(self):
        return "Eiki"

    def max_value(self, board, action, alpha, beta, player_code, p):
        if (p==0):
            return self.eval(player_code, board), action
        sucessores = self.sucessores(player_code, board)
        for s in sucessores:
            mv, ac = self.min_value(s['board'], s['action'], alpha, beta, player_code, p-1)
            if (mv > alpha):
                alpha  = mv
                action = ac
            if (alpha >= beta):
                return alpha, action
        return alpha, action

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

    def eval(self, player, board): 
        my_points_line = self.count_row_line(player, board)
        my_points_col = self.count_row_column(player, board)
        my_points_dig = self.count_row_diag(player, board)
        my_points_dig2 = self.count_row_diag(player, board[::-1])
        my_qtd_2 = my_points_line['2'] + my_points_col['2'] + my_points_dig['2'] + my_points_dig2['2']
        my_qtd_3 = my_points_line['3'] + my_points_col['3'] + my_points_dig['3'] + my_points_dig2['3']
        my_qtd_4 = my_points_line['4'] + my_points_col['4'] + my_points_dig['4'] + my_points_dig2['4']
        sum_my_points = 100000*my_qtd_4 + 100*my_qtd_3 + my_qtd_2

        opponent = self.opponent(player)
        op_points_line = self.count_row_line(opponent, board)
        op_points_col = self.count_row_column(opponent, board)
        op_points_dig = self.count_row_diag(opponent, board)
        op_points_dig2 = self.count_row_diag(opponent, board[::-1])
        op_qtd_2 = op_points_line['2'] + op_points_col['2'] + op_points_dig['2'] + op_points_dig2['2']
        op_qtd_3 = op_points_line['3'] + op_points_col['3'] + op_points_dig['3'] + op_points_dig2['3']
        op_qtd_4 = op_points_line['4'] + op_points_col['4'] + op_points_dig['4'] + op_points_dig2['4']
        sum_op_points = 100000*op_qtd_4 + 10000*op_qtd_3 + op_qtd_2
        
        return sum_my_points - sum_op_points

    def is_movable(self, board, action):
        for i in range(5,-2,-1):
            if (board[i,action] == 0):
                break
        if(i<0):
            return False
        return True

    def need_block(self, board):
        flag = False
        for i in range(6):
            current = None
            counter = 0
            for j in range(6):
                if ((board[i, j] in (1,2)) and (board[i, j] == board[i, j + 1])):
                    if (board[i, j]==current):
                        counter = counter + 1
                        current = board[i, j]
                        if (counter==2):
                            
                            return True
                            
                    else:
                        counter = 1
                        current = board[i, j]
                else:
                    counter = 0
        # verticallyel
        for i in range(7):
            current=None
            counter = 0
            for j in range(5):
                if ((board[j, i] in (1,2)) and (board[j,i] == board[j+1,i])):
                    if(board[j,i]==current):
                        counter = counter + 1
                        if (counter==2):
                            return True
                        current = board[j,i]
                    else:
                        counter = 1
                        current = board[j,i]
                else:
                    counter = 0
        # "main" diagonal
        for k in range(-2,4):
            current = None
            counter = 0
            x = np.diag(board, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] != 0) and (x[i] == x[i+1])):
                    if(x[i] == current):
                        counter = counter + 1
                        if (counter == 2):
                            return True
                        current = x[i]
                    else:
                        counter = 1
                        current = x[i]
                
        # "anti" diagonal
        # [::-1] rotaciona as linhas da matriz
        temp = board[::-1]
        for k in range(-2,4):
            current = None
            counter = 0
            x = np.diag(temp, k=k)
            for i in range(0,len(x)-1):
                if ((x[i] != 0) and (x[i] == x[i+1])):
                    if(x[i] == current):
                        counter = counter + 1
                        if (counter == 2):
                            return True
                        current = x[i]
                    else:
                        counter = 1
                        current = x[i]

        return False

    def move(self, player_code, board):
        
        result = EikiPlayer.classifier.predict(self.transform_shape(board))
        classifier_action = np.argmax(result)
        need_block = self.need_block(board)

        if not self.is_movable(board, classifier_action) or need_block:
            print("Entrou")
            _, action = self.max_value(board, None, -999999, 999999, player_code, 5)
            return None, action
        print(classifier_action)
        return None, classifier_action

    def movement(self, player, board, column):
        result_board = np.matrix(board)
        for i in range(5,-2,-1):
            if (board[i,column] == 0):
                break
        if(i<0):
            return None
        result_board[i, column] = player
        return result_board

    

    

