from SearchAlgorithms import BuscaCustoUniforme
from U2 import U2

def test_menor_caminho():
    state = U2(False, False, False, False, False, ' ')
    algorithm = BuscaCustoUniforme()
    result = algorithm.search(state)
    assert result.g <= 17
    print(result.show_path())