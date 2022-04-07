from SearchAlgorithms import BuscaProfundidadeIterativa, BuscaProfundidade, BuscaLargura
from Graph import State
import math
import warnings
warnings.filterwarnings("ignore")

#
# Knuth conjecturou em 1964 que, começando com o número 4, uma sequência
# de fatoriais, raiz quadrada e operações de arrendondamento para baixo 
# é possível chegar a qualquer inteiro positivo desejado. 
#

class KnuthProblem(State):

    limite_fatorial = 500000

    def __init__(self, number, goal, op):
        self.number = number
        self.goal = goal
        self.operator = op
    
    def sucessors(self):
        sucessors = []
        sucessors.append(KnuthProblem(math.trunc(self.number), self.goal, 'round_down'))
        try:
            sucessors.append(KnuthProblem(math.sqrt(self.number), self.goal, 'sqrt'))
        except OverflowError:
            #print('overflow error', self.number)
            pass
        try:
            if self.number < self.limite_fatorial:
                sucessors.append(KnuthProblem(math.factorial(self.number), self.goal, 'factorial'))
        except ValueError:
            pass
        return sucessors
            
    def is_goal(self):
        return self.number == self.goal
    
    def description(self):
        return """Começando com o número 4, uma
        sequência de fatoriais, raiz quadrada e operações de 
        arrendondamento para baixo é possível chegar a qualquer 
        inteiro positivo desejado."""
    
    def cost(self):
        return 1

    def print(self):
        return str(self.operator)
    
    def env(self):
        #return str(self.number) + " # " + str(self.operator)
        return self.number

    def h(self):
        return (abs(self.goal - self.number))


def main():
    print('Iniciando busca... ')
    state = KnuthProblem(4, 10, '')
    #algorithm = BuscaProfundidadeIterativa()
    algorithm = BuscaProfundidade()
    result = algorithm.search(state, 10)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')

if __name__ == '__main__':
    main()