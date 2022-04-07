from SearchAlgorithms import AEstrela
from Puzzle8 import Puzzle8
from datetime import date, datetime

tabuleiro_facil = [[8,1,3],[0,7,2],[6,5,4]]
tabuleiro_dificil0 = [[8,3,6],[7,5,4],[2,1,0]]
tabuleiro_dificil1 = [[7,8,6],[2,3,5],[1,4,0]]
tabuleiro_dificil2 = [[7,8,6],[2,3,5],[0,1,4]]
tabuleiro_impossivel1 = [[3,4,8],[1,2,5],[7,0,6]]
tabuleiro_impossivel2 = [[5,4,0],[6,1,8],[7,3,2]]

def test_facil():
    print('facil')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_facil, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; direita ; direita ; baixo ; esquerda ; esquerda ; cima ; cima ; direita ; baixo"

def test_dificil0():
    print('dificil 0')    
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil0, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; cima ; cima ; esquerda ; baixo ; esquerda ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; baixo ; direita ; cima ; direita ; baixo ; esquerda ; cima ; cima ; esquerda ; baixo ; direita"

def test_dificil1():
    print('dificil 1')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil1, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; cima ; esquerda ; baixo ; esquerda ; cima ; cima ; direita ; direita ; baixo ; esquerda ; esquerda ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; baixo ; direita ; cima ; cima ; esquerda ; baixo ; direita"

def test_dificil2():
    print('dificil 2')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_dificil2, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == " ; cima ; cima ; direita ; baixo ; esquerda ; baixo ; direita ; cima ; direita ; cima ; esquerda ; esquerda ; baixo ; baixo ; direita ; cima ; direita ; baixo ; esquerda ; cima ; cima ; esquerda ; baixo ; direita"

def test_impossivel1():
    print('impossivel 1')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_impossivel1, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == "Nao tem solucao"

def test_impossivel2():
    print('impossivel 2')
    inicio = datetime.now()
    state = Puzzle8(tabuleiro_impossivel2, '')
    r = state.show_path()
    fim = datetime.now()
    print(fim - inicio)
    assert r == "Nao tem solucao"

