---
title: Agente Autônomo
subtitle: Fevereiro de 2022
author: Fabrício Barth 
institute: Agentes Autônomos e Aprendizagem por Reforço
date: 02/2022
theme: insper
aspectratio: 169
...

## Definição: Russel and Norvig, cap. 02 do AIMA

:::::::::::::: {.columns}
::: {.column width="50%"}

Um agente é qualquer coisa que pode ser visualizada como percebendo o ambiente através de sensores e agindo sobre o ambiente através de atuadores.

\vspace{0.5cm}

\begin{center}
\includegraphics[width=0.8\textwidth]{figuras/agent_01.png}
\end{center}

:::
::: {.column width="50%"}

\includegraphics[width=1\textwidth]{figuras/agente.png}

:::
::::::::::::::

## Definição Maes, 1995

:::::::::::::: {.columns}
::: {.column width="50%"}

Agentes autônomos são **sistemas computacionais** que habitam algum **ambiente complexo e dinâmico**, percebem e agem de maneira **autônoma** sobre este ambiente, para realizar um conjunto de **tarefas** e **objetivos** para o qual ele foi projetado.

:::
::: {.column width="50%"}

\includegraphics[width=1\textwidth]{figuras/agent_02.png}

:::
::::::::::::::

## Definição Wooldridge & Jennings, 1995

Uma entidade de hardware ou software que possui as seguintes propriedades:

* **autonomia**: agentes devem operar sem a intervenção direta de pessoas ou outros agentes e devem possuir controle sobre suas próprias ações e sobre o seu estado interno;

* **habilidade social**: agentes devem ter capacidade de interagir com outros agentes, possivelmente pessoas, através de algum tipo de linguagem ou protocolo de comunicação;

##

* **reatividade**: agentes devem perceber o ambiente onde estão inseridos (pode ser o mundo físico, o usuário através de uma interface gráfica, um grupo de agentes, a Internet ou todos estes objetos combinados), e;

* **pró-ativo**: agentes não devem simplesmente agir apenas em resposta ao ambiente, eles devem ter a capacidade de tomar a iniciativa para a execução de um determinado objetivo.

## Exemplos

* Jogador de jogos de tabuleiro.

* Assistentes Virtuais.

* Sistemas de Recomendação.

* Veículos Autônomos. 

* Classificadores automático de conteúdo. 

# É possível saber a diferença entre um agente autônomo e um sistema convencional?

## Um pouco de formalismo segundo Silver, 2021

:::::::::::::: {.columns}
::: {.column width="50%"}

Um **agente** é um sistema que recebe no tempo $t$ uma observação $O_{t}$ e gera uma saída 
$A_{t}$. 

\vspace{0.2cm}

Ou seja, um agente é um sistema $A_{t} = \alpha(H_{t})$ que seleciona uma ação $A_{t}$ em um tempo $t$ dado uma história $H_{t} = O_{1},A_{1}, \cdots, O_{t-1},A_{t-1},O_{t}$. 

\begin{eqnarray}
O_{i} = s \nonumber \\ 
s \in S \nonumber \\ 
A_{i} = a \in A \nonumber
\end{eqnarray}

:::
::: {.column width="50%"}

\includegraphics[width=1\textwidth]{figuras/agent_02.png}

:::
::::::::::::::

##

:::::::::::::: {.columns}
::: {.column width="50%"}

Um **ambiente** é um sistema que recebe uma ação $A_{t}$ no tempo $t$ e responde com
uma observação $O_{t+1}$.

\vspace{0.5cm}

Ou seja, um ambiente é um sistema $O_{t+1} = \varepsilon(H_{t}, A_{t}, n_{t})$

\vspace{0.2cm}

* $H_{t}$ é um estado que acumula toda a história;
* $A_{t}$ é a última ação do agente;
* $n_{t}$ *potencialmente* é uma fonte de aleatoriedade. 

:::
::: {.column width="50%"}

\includegraphics[width=1\textwidth]{figuras/agent_02.png}

:::
::::::::::::::

## Propriedades do ambiente

* **Acessível ou inacessível**: quando o agente tem percepção de todo ambiente, ou pelo menos das variáveis de seu interesse.

* **Determinístico ou indeterminístico**: se o próximo estado é completamente determinado pelo estado atual e a ação selecionada pelo agente.

* **Síncrono ou assíncrono**: é um ambiente que não muda enquanto o agente está deliberando.

* **Discreto ou contínuo**: um número limitado e bem definido de percepções e ações.

* **Single Agent ou Multi-agent**: neste caso podemos ter ambientes *multi-agent* competitivos ou colaborativos. 

* **Competitivo ou colaborativo**: o agente está competindo ou colaborando com outros agentes?

## Quais são as propriedades destes ambientes?

* **Xadrez com relógio**: 

* **Xadrez sem relógio**: 

* **Veículo autônomo**: 

* **Futebol de robôs**: 

## Exemplos de propriedades de ambientes

* **Xadrez com relógio**: acessível, determinístico, assíncrono, discreto, single agent e competitivo.

* **Xadrez sem relógio**: acessível, determinístico, síncrono, discreto, single agent e competitivo.

* **Veículo autônomo**: inacessível, indeterminístico, assíncrono, contínuo, multi-agent e colaborativo. 

* **Futebol de robôs**: acessível, indeterminístico, assíncrono, contínuo, multi-agent e colaborativo/competitivo. 

# Por que identificar as propriedades de um ambiente é relevante?

## Referências

* Franklin S., Graesser A. It is an Agent, or just a program? A Taxonomy for Autonomous Agents. 1996.

* Russell, S., Norvig P. Inteligência Artificial. Segunda Edição. Cap. 02.

* SILVER, D.; SINGH S.; PRECUP D.; SUTTON R. [Reward is enough](https://doi.org/10.1016/j.artint.2021.103535). Artificial Intelligence. Vol 299, 2021.