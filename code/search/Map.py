from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from Graph import State
import time
import networkx as nx
import csv

class Map(State):

    def __init__(self, city, cost, op, goal):
        self.city = city
        self.cost_value = cost
        self.operator = op
        self.goal = goal
    
    def sucessors(self):
        sucessors = []
        # TODO
        pass
    
    def is_goal(self):
        return (self.city == self.goal)
    
    def description(self):
        return "Encontrando o menor caminho entre cidades"
    
    def cost(self):
        pass
    
    def print(self):
        pass
    
    def env(self):
        pass


    @staticmethod
    def createArea():
        #
        # TODO mover a definicao do mapa de uma forma hard-coded para para leitura
        # a partir de um arquivo. 
        # 
        Map.area = {
            'a':[(3,'b'),(6,'c')],
            'b':[(3,'a'),(3,'h'),(3,'k')],
            'c':[(6,'a'),(2,'g'),(3,'d'),(2,'o'),(2,'p')],
            'd':[(3,'c'),(1,'f'),(1,'e')],
            'e':[(2,'i'),(1,'f'),(1,'d'),(14,'m')],
            'f':[(1,'g'),(1,'e'),(1,'d')],
            'g':[(2,'c'),(1,'f'),(2,'h')],
            'h':[(2,'i'),(2,'g'),(3,'b'),(4,'k')],
            'i':[(2,'e'),(2,'h')],
            'l':[(1,'k')],
            'k':[(1,'l'),(3,'n'),(4,'h'),(3,'b')],
            'm':[(2,'n'),(1,'x'),(14,'e')],
            'n':[(2,'m'),(3,'k')],
            'o':[(2,'c')],
            'p':[(2,'c')],
            'x':[(1,'m')]
            }


def main():

    Map.createArea()
    state = Map('i', 0, 'i', 'x')
    algorithm = None #TODO

    ts = time.time()
    result = algorithm.search(state)
    tf = time.time()
    if result != None:
        print(result.show_path())
    else:
        print('Nao achou solucao')
    print('Tempo de processamento em segundos: ' + str(tf-ts))
    print('O custo da solucao eh: '+str(result.g))
    print('')
    
if __name__ == '__main__':
    main()
