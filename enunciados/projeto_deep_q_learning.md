# Projeto de Q-Learning e Deep Q-Learning

A base teórica e prática sobre o que conhecemos hoje em dia sobre Deep Reinforcement Learning é apresentada nesta sequência de artigos: 

1. [Playing Atari with Deep Reinforcement Learning](https://arxiv.org/abs/1312.5602), Mnih et al., 2013
2. [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236), Mnih et al., 2015
3. [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461), van Hasselt et al., 2015

Em sala de aula já utilizamos o que foi proposto em [[1](https://arxiv.org/abs/1312.5602)] para implementar um agente que consegue resolver o problema do *CartPole*. O objetivo deste projeto é replicar o que foi proposto em [[1](https://arxiv.org/abs/1312.5602)], [[2](https://www.nature.com/articles/nature14236)] e [[3](https://arxiv.org/abs/1509.06461)] considerando alguns ambientes do OpenAI Gym. 

O escopo deste projeto está dividido em três partes: básica, avançada e proficiente. 

## Entrega Básica

O objetivo da entrega básica é desenvolver um agente que consegue controlar um aterrissador lunar ([Lunar Lander](https://www.gymlibrary.ml/environments/box2d/lunar_lander/)) usando o que foi proposto nos artigos citados acima. Esta entrega deve possuir:

* um script que treina o agente usando o algoritmo proposto por [[1](https://arxiv.org/abs/1312.5602)] e [discutido em sala de aula](https://github.com/fbarth/reinLearn/blob/main/slides/deep_reinforcement_learning.md);

* um resumo do processo de treinamento na forma de uma imagem. Esta imagem deve apresentar os episódios versus o indicador escolhido pelo aluno para a avaliar o processo de aprendizagem; 

* um script que faz a leitura do modelo treinado e testa o agente em um estado inicial aleatório. O script que realiza o treino do agente deve persistir o modelo treinado para que outro script faça o uso deste modelo. A forma como os scripts irão gravar e ler o modelo fica a critério do aluno;

* um script que treina o agente usando o algoritmo proposto por [[3](https://arxiv.org/abs/1509.06461)]. Este script pode ser uma versão a partir do código [DeepQLearning.py](https://github.com/fbarth/reinLearn/blob/main/src/parte6/DeepQLearning.py), pode ser um script que utilizada a implementação [DQNAgent](https://keras-rl.readthedocs.io/en/latest/agents/dqn/) da biblioteca Keras ou pode ser qualquer outra implementação desde que devidamente referenciada e justificada; 

* um resumo do processo de treinamento na forma de uma imagem. Esta imagem deve apresentar os episódios versus o indicador escolhido pelo aluno para avaliar o processo de aprendizagem; 

* o script que realiza o treino do agente deve persistir o modelo treinado para que outro script faça o uso deste modelo. A forma como os scripts irão gravar e ler o modelo fica a critério do aluno;

* um breve texto que compara o processo de aprendizagem dos dois algoritmos e os resultados encontrados. 

## Entega Proficiente

O objetivo da entrega proficiente é desenvolver um agente que consegue jogar o jogo **Breakout** do Atari. Este ambiente é discutido em todos os artigos citados acima. Inclusive, em [[2](https://www.nature.com/articles/nature14236)] os autores descrevem todos os hiperparâmetros utilizados para treinar um agente que tem habilidades superiores a de humanos neste jogo.  Para entregar este item o aluno deverá: 

* implementar um script que treina o agente usando qualquer um dos algoritmos ou implementações vistos até o momento. Lembre-se que neste caso as dimensões utilizadas para representar cada estado são diferentes do problema do *Lunar Land*; 

* um texto que descreve o resumo do processo de treinamento: quais foram os hiperparâmetros utilizados, que estrutura de rede neural foi utilizada e quais os resultados alcançados. Tente utilizar no mínimo uma imagem para sumarizar os resultados alcançados durante a etapa de treinamento;

* um script que é capaz de ler o modelo e executar o agente no ambiente.

## Entrega Avançada

O objetivo da entrega avançada é treinar um agente que pode alcançar um nível sobre-humano no **Space Invaders** do Atari. Os mesmos itens que são solicitados na *entrega proficiente* também são solicitados aqui.  

# Regras e atribuição das notas

* A entrega básica é pré-requisito para as demais entregas. 
* A entrega proficiente é pré-requisito para a entrega avançada. 
* O aluno que entregar todos os itens da entrega básica tem conceito C nesta avaliação.
* O aluno que entregar todos os itens da entrega básica e todos os itens da entrega proficiente tem conceito B nesta avaliação.
* O aluno que entregar todos os itens das entregas básica, proficiente e avançado tem conceito A+ nesta avaliação.

# Data e formato de entrega

Este trabalho é um trabalho **individual** e deverá ser entregue via um **repositório privado no GitHub**. O aluno deverá convidar o professor da disciplina e deverá manter este repositório privado até o final do semestre. Depois, se for da vontade do aluno, o respositório poderá se tornar público. 

A data máxima para entrega deste projeto é **29/05/2022** (domingo).




