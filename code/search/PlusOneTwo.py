from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import AEstrela
from Graph import State

#
# Initial state: 1
# Operations: +1 and +2
# Final state: any number bigger than 0
#

class PlusOneTwo(State):

    def __init__(self, number, op, Goal):
        self.number = number
        self.operator = op
        self.Goal = Goal

    def env(self):
        pass
    
    def sucessors(self):
        pass
    
    def is_goal(self):
        return False
    
    def description(self):
        return "Problema simples com operadores de soma 1 e soma 2. Estados representados apenas por um numero"
    
    def cost(self):
        return 1

    def h(self):
        return 0
    
    def print(self):
        return str(self.operator)

from datetime import datetime

def main():
    
    #
    # Executando busca em largura
    #
    print('Busca em largura')
    state = PlusOneTwo(1, '', 10)
    algorithm = BuscaLargura()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    if result != None:
        print('Achou!')
        print(result.show_path())
    else:
        print('Nao achou solucao')


if __name__ == '__main__':
    main()
