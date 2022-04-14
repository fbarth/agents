# Implementações sobre Jogos de Tabuleiro e Busca Competitiva

Nesta pasta você irá encontrar arquivos que implementam o Jogo Liga4 (em inglês, *four in a row* ou *Connect4*) e o jogo da velha. 

## Jogo da velha

O jogo da velha é um jogo extremamente simples e amplamente conhecido, não necessitando descrições. 

Na pasta `tictactoe` você irá encontrar os seguintes arquivos: 

* [tictactoe/JogoVelha.py](tictactoe/JogoVelha.py): implementa as regras e controles do jogo da velha;
* [tictactoe/TournamentJV.py](tictactoe/TournamentJV.py): define um campeonato de ida e volta entre vários jogadores;
* [tictactoe/Player.py]: define a interface que cada implementação de jogador deve seguir;
* [tictactoe/PlayerSpecificationJV.py](tictactoe/PlayerSpecificationJV.py): trata-se de um exemplo de como cada participante do campeonato deve codificar o seu jogador;
* [tictactoe/BarthJV.py](./tictactoe/BarthJV.py) e [tictactoe/CaioSamuel.py](./tictactoe/CaioSamuel.py): são exemplos de implementações de jogadores;
* além disso, no diretório [tictactoe](./tictactoe/) é possível encontrar alguns arquivos de testes usando `pytest` que começam com `test_`.

As regras para a competição são:

* Cada jogador só pode realizar movimentos válidos. Se um jogador realizar qualquer movimento inválido então ele será desclassificado da competição e, consequentemente, ficará em último lugar na competição.

* Todos os movimentos precisam ter uma duração máxima de 2 segundos.

* O campeonato será composto por jogos de ida e volta, ou seja, todo jogador jogará duas vezes contra o mesmo adversário. Sendo que em uma partida um jogador começa e na outra partida outro jogador começa. 

* Nenhum jogador poderá perder do jogador aleatório. Se perder do jogador aleatório então o competidor será posto em último lugar na competição.


## Jogo Liga4

O Jogo Liga4 (em inglês, *four in a row*) é um jogo de tabuleiro jogado por duas pessoas, sem variável aleatória e de soma zero. Ou seja, um jogador pode ganhar, empatar ou perder o jogo. 

O jogo é jogado em um tabuleiro com 7 colunas e 6 linhas colocado na vertical. Cada jogador tem peças de uma só cor. O jogo consiste em escolher em qual coluna colocar a sua peça. Quem alinhar 4 de suas peças na horizontal, vertical ou qualquer uma das diagonais vence. Neste site é possível jogar este jogo contra uma pessoa ou contra uma máquina: https://www.coolmathgames.com/0-4-in-a-row. Ao ver como o o jogo funciona em https://www.coolmathgames.com/0-4-in-a-row fica mais fácil entender as suas regras e objetivos. 

No diretório [fourinrow](./fourinrow/) temos cinco arquivos que estão relacionados com o jogo Liga4: 

* [FourInRow.py](./fourinrow/FourInRow.py): define todas as regras e gerencia o jogo. Para iniciar um jogo é necessário instanciar um objeto desta classe, passando dois jogadores, e executando o método `game()`:

````python
FourInRow(ManualPlayer(), RandomPlayer()).game()
````

Neste caso, foi instanciado um jogo onde um jogador manual joga contra um robô que tem os seus movimentos definidos de forma aleatória. 

* [Player.py](./fourinrow/Player.py): define uma classe abstrata que possui dois métodos: 

````python   
@abstractmethod
def move(self, player_code, board):
    pass

@abstractmethod
def name(self):
    pass
````

Todos os jogadores precisam implementar o método `move` e o retorno deste método precisa ser um número entre 0 e 6 que é o índice da coluna onde será jogada a peça do jogador. 

* [ManualPlayer.py](./fourinrow/ManualPlayer.py): define um jogador manual. A implementação do método `move` nesta classe é apenas a leitura do índice da coluna pelo teclado: 

````python
def move(self, player_code, board):
    g = input("Enter a column (0..6) : ") 
    return int(g)
````

* [RandomPlayer.py](./fourinrow/RandomPlayer.py): define um jogador que joga de forma aleatória. O método `move` deste jogador esta implementado da seguinte forma: 

````python
def move(self, player_code, board):
        return randint(0, 6)
````

* [PlayerSpecification.py](./fourinrow/PlayerSpecification.py): é um exemplo de como você deve começar a sua implementação. 

### Execução do campeonato

````bash
python Tournament.py > logs/competicao_results.log &
````

### Análise dos resultados

Para verificar quem venceu de quem:

````bash
cat logs/competicao_results.log | grep -e 'winner\|vs'  
````

Para identificar quem ultrapassou o limite de 15 segundos por jogada:

````bash
cat logs/competicao_results.log | grep -e 'duration' 
````

### Regras do campeonato

* O campeonato se formado por turno e re-turno, todos contra todos. Vitória é igual a dois pontos, Empate igual a um ponto e Derrota igual a zero pontos.
* Um dos jogadores da competição será o jogador aleatório. Nenhum jogador poderá perder do jogador aleatório. O jogador que perder do jogador aleatório será desclassificado e ficará automaticamento em último lugar na competição. 
* Nenhum jogador poderá fazer uma jogada inválida (selecionar um número maior que 6 ou menor que 0, ou selecionar uma coluna já cheia). Se o jogador fizer uma jogada inválida também será automaticamente desclassificado e ficará em último lugar na competição. 
* Cada jogada terá no máximo 15 segundos de tempo. Se um jogador ultrapassar este tempo então também será automaticamente desclassificado da competição. 

## Jogo Liga4 com PopOut

Trata-se de uma variante do Liga4 onde além de adicionar peças em cada coluna é possível também remover peças que estão na base das colunas, desde que tais peças sejam do jogador. 

As implementações têm a mesma estrutura do jogo convencional de Liga4. O enunciado para o projeto pode ser acessado [aqui](../../enunciados/implementacao_busca_competitiva.md).





