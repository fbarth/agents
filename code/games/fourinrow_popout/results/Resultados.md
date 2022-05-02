# Resultados da competição de Connect4 variante com popout

Durante a aula do dia 28/04/2022 foram feito os ajustes dos agentes para a competição e depois destes ajustes, ao longo do final de semana, foram executadas 2 competições. O log de cada competição pode ser visto neste diretório. Arquivos com o padrão `log_campeonato_rodada[N].txt` possuem o log completo da competição. Arquivos com o padrão `log_error_campeonato_rodada[N].txt` descrevem os eventuais erros que aconteceram durante a competição. 

Os seguintes jogadores participaram da competição:

````python
    RandomPlayer(),
    BarthPlayer(),
    #PedroPlayer(),
    MCTSPlayer(),
    GZPlayer(),
    GabiiPlayer(),
    FuziyPlayer(),
    AutoPlayer(),
    MyPlayer(),
    #ThomePlayer(),
    MiniPlayer(),
    GabrielPlayer(),
    EikiPlayer()
````

Sendo que os jogadores `RandomPlayer` e `BarthPlayer` não serão avaliados. Os jogadores `PedroPlayer` e `ThomePlayer` foram removidos da competição pois eles estavam executando movimentos não permitidos. 

Os resultados das duas competições foram: 

````
{
    'Random': 0, 
    'Barth': 6, 
    'Carlos Monteiro (8, 1)': 18, 
    'GZ Player': 18, 
    'Gabii': 12, 
    'Fuziy Player': 12.0, 
    'AutoPlayer': 17, 
    'Victor Vergara': 7.5, 
    'Mini': 10.5, 
    'Gabriel M': 6, 
    'Eiki': 3}
````

````
{
    'Random': 2, 
    'Barth': 6, 
    'Carlos Monteiro (8, 1)': 18, 
    'GZ Player': 20, 
    'Gabii': 11, 
    'Fuziy Player': 12.0, 
    'AutoPlayer': 16, 
    'Victor Vergara': 7.5, 
    'Mini': 10.5, 
    'Gabriel M': 6, 
    'Eiki': 1}
````

O único jogador que perde para o jogador aleatório é o `Eiki`. Para ver isto basta executar o comando abaixo:

````bash
cat results/log_campeonato_rodada5.txt| grep -e 'winner\|vs' | grep -e Random
````

Para ver detalhes dos resultados da competição competição, basta digitar: 

````bash
cat results/log_campeonato_rodada4.txt| grep -e 'winner\|vs'
cat results/log_campeonato_rodada5.txt| grep -e 'winner\|vs'
````

Ou simplesmente dar um `cat` nos logs do campeonato. 

Não teve nenhum jogador que ultrapassou o limite de 10 segundos. Ao executar os seguintes comandos: 

````bash
cat results/log_campeonato_rodada4.txt| grep -e 'duration'
cat results/log_campeonato_rodada5.txt| grep -e 'duration'
````

Nenhum output é apresentado. Apenas o jogador `AutoPlayer` teve que ajustar a sua profundidade de 10 para 9. 

**O ranking final da competição foi**: 

* Primeiro colocado: GZPlayer
* Segundo colocado: Carlos Monteiro (8, 1)
* Terceiro colocado: AutoPlayer

As notas, considerando o resultado da competição, aspectos de inovação e documentação, serão enviadas individualmente via BlackBoard. 