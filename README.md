# Agentes Autônomos e Aprendizagem por Reforço

Este projeto possui o material da disciplina sobre Agentes Autônomos e 
Aprendizagem por Reforço (*Reinforcement Learning*).

## Publicar nova versão da página web

Para publicar o novo conteúdo da página web basta fazer um `push` para o branch gh-pages:

````bash
git push origin main:gh-pages
````

No repositório existe uma action configurada para fazer o deploy do conteúdo na página [http://fbarth.net.br/agents/](http://fbarth.net.br/agents/).

## Compilando material escrito em Markdown

Segue um exemplo sobre como compilar os materiais que estão em markdown: 

````bash
pandoc -t beamer introducao_ia.md -o  introducao_ia.pdf
````
