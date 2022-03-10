# Diário de bordo da disciplina

* 10/03: Status sobre os problemas discutidos em sala de aula e novos problemas:

    * Aspirador de pó com 2 e 3 quartos: espera-se que **TODOS** tenham entendido e implementado a solução;
    * Soma +1 e +2: espera-se que **TODOS** tenham entendido e implementado a solução, inclusive utilizando o conceito de heurística;
    * Banda U2: espera-se que **TODOS** tenham entendido a solução;
    * Conjectura de Knuth: espera-se que **TODOS** tenham entendido o problema e **ALGUNS** sofrendo com detalhes de implementação;
    * Cavalo no tabuleiro de Xadrez: foram adicionadas algumas referências que talvez possam ajudar no desenvolvimento da solução;
    * Caminhos entre cidades: este é fácil de implementar. Já discutimos em sala de aula. Precisa implementar com heurística, apesar do exemplo ter
    um espaço de busca pequeno. Tem alguns detalhes sobre leituras de arquivos e algumas estruturas de dados um pouco mais complexas (grafos)
    que talvez gere um esforço adicional;
    * Problema das oito rainhas: este é **NOVO**. Quando chegar nele me avisa! 
    * 

* 08/03: Discutir o conceito de heurística ([do slide 32 até 41](./slides/03_algoritmos_busca/busca_versaoFabricio.pdf)) 
e algoritmos de busca informados visando resolver os problemas em aberto 
do [enunciado 1](./enunciados/implementacoes_busca_parte1.md) e no [enunciado 2](./enunciados/implementacoes_busca_parte2.md). Problemas discutidos:
    * Aspirador de pó com 2 e 3 quartos;
    * Soma +1 e +2;
    * Banda U2;
    * Conjectura de Knuth;
    * Cavalo no tabuleiro de Xadrez;
    * Caminhos entre cidades;
    * 
 
* 03/03: Vamos continuar o problema da banda U2 e conjectura de Knuth. Resumo do dia: 

<img src="img/resumo_030322.jpeg" alt="Resumo" width="400"/>

Tem código novo no projeto! Melhor fazer um *git pull*.

* 24/02: Vamos começar a implementar soluções para alguns problemas clássicos de otimização, roteamento e planejamento. O enunciado com as questões está neste [arquivo](./enunciados/implementacoes_busca_parte1.md). Fizemos os exercícios do aspirador de pó, aspirador de pó com 3 quartos, soma 1 e soma 2 com explicação sobre heurística.

* 22/02: Vimos como definir um problema usando espaço de busca (estados, transições, estado meta e custo) [[referência]](slides/03_algoritmos_busca/busca_versaoFabricio.pdf). Relembramos o funcionamento dos algoritmos de Busca em Largura e Profundidade. Vimos os algoritmos Busca em Profundidade Iterativo e Busca de custo uniforme. Também analisamos tais algoritmos considerando os critérios: completo, ótimo, tempo, espaço. 

* 17/02: Vamos definir melhor o que é [agente autônomo e ambiente](slides/02_agentes_autonomos/agentes_autonomos.pdf). E provavelmente vamos começar a ver uma das formas que podemos utilizar para [modelar e implementar agentes autônomos](slides/03_algoritmos_busca/busca_versaoFabricio.pdf). 
    * [What's the status of self-driving cars? There has been progress, but safety questions remain.](https://www.cbsnews.com/news/self-driving-cars-status-progress-technology-safety/)

* 15/02: Apresentação dos objetivos, dinâmica e materiais da disciplina. Discussão sobre o que é [IA e a relação com agentes autônomos](slides/01_introducao_ia/introducao_ia.pdf). Além das referências já disponibilizadas no material, também foram discutidas outras referências, entre elas:
    * [Game over: Kasparov and The Machine, 2003](https://www.imdb.com/title/tt0379296/)
    * [Deep Blue - Down the Rabbit Hole](https://www.youtube.com/watch?v=HwF229U2ba8): um vídeo um tanto quanto interessante sobre o assunto com vários detalhes que são difíceis de encontrar em outras fontes. 
    * [AlphaGo - The Movie, 2020](https://www.youtube.com/watch?v=WXuK6gekU1Y)
    * [Game Changer: AlphaZero's Groundbreaking Chess Strategies and the Promise of AI, 2019](https://www.amazon.com.br/dp/B07N6G7X5V)
    * [Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess](https://arxiv.org/abs/2009.04374)  