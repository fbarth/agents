from SearchAlgorithms import BuscaLargura
from SearchAlgorithms import BuscaProfundidade
from SearchAlgorithms import BuscaProfundidadeIterativa
from SearchAlgorithms import BuscaCustoUniforme
from SearchAlgorithms import BuscaGananciosa
from SearchAlgorithms import AEstrela
from KnuthProblem import KnuthProblem
from datetime import date, datetime

def test_24():
    state = KnuthProblem(4, 24, '')
    algorithm = BuscaProfundidadeIterativa()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; factorial"

def test_620448401733239439360000():
    state = KnuthProblem(4, 620448401733239439360000, '')
    algorithm = BuscaProfundidadeIterativa()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; factorial ; factorial"

def test_787685471322():
    state = KnuthProblem(4, 787685471322, '')
    algorithm = BuscaProfundidadeIterativa()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; factorial ; factorial ; sqrt ; round_down"

def test_942():
    state = KnuthProblem(4, 942, '')
    algorithm = BuscaProfundidadeIterativa()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; factorial ; factorial ; sqrt ; sqrt ; sqrt ; round_down"

def test_942():
    state = KnuthProblem(4, 30, '')
    algorithm = BuscaProfundidadeIterativa()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; factorial ; factorial ; sqrt ; sqrt ; sqrt ; sqrt ; round_down"

def test_1():
    state = KnuthProblem(4, 1, '')
    algorithm = BuscaProfundidadeIterativa()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; sqrt ; sqrt ; round_down"

def test_2():
    state = KnuthProblem(4, 2, '')
    algorithm = BuscaProfundidadeIterativa()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; sqrt"

def test_5():
    state = KnuthProblem(4, 5, '')
    algorithm = BuscaProfundidadeIterativa()
    inicio = datetime.now()
    result = algorithm.search(state)
    fim = datetime.now()
    print(fim - inicio)
    assert result.show_path() == " ; factorial ; factorial ; sqrt ; sqrt ; sqrt ; sqrt ; sqrt ; round_down"
