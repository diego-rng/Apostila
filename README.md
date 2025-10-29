# Apostila No. 1

Esse repositório é dedicado à primeira apostila da Renova. Para essa apostila eu decidi usar a linguagem Python.

A Apostila consiste de 26 exercícios.

# Índice

1. **[Exercícios](#Exercícios)**
    1. [Exercício 1 - Exame Chunin](#exame-chunin)
    2. [Exercício 2 - Continha](#continha)
    3. [Exercício 3 - Desenhista](#desenhista)
    4. [Exercício 4 - Incursão da Divisão de Reconhecimento](#incursão-da-divisão-de-reconhecimento)
    5. [Exercício 5 - Drone da Amazônia](#drone-da-amazônia)




# Exercícios
***
## Exame Chunin
A Aldeia da Folha deu início ao Exame Chunin! Nele, dezenas de ninjas dividiram-se em trios para disputar dois pergaminhos. Cada equipe iniciará a etapa do exame com um pergaminho, precisando lutar para conquistar outro pergaminho, mas precisa ser um de cada tipo para que possam se classificar para a segunda fase. Baseado nisso, seu programa deverá avisar se o trio de Naruto Uzumaki, Sasuke Uchiha e Sakura Haruno foram classificados ou eliminados do Exame Chunin.

### Entrada
A entrada é composta por dois caracteres “P1” e “P2”, dados em linhas diferentes e representando a característica de cada pergaminho. Portanto, “P1” e “P2” podem ser “A” (azul), “B” (branco) e “N” (sem pergaminho).

### Saída
A saída será composta pela mensagem “classificado”, indicando que o trio foi classificado (dois pergaminhos distintos) ou “eliminado” (pergaminhos iguais ou pelo menos um pergaminho faltando), indicando a eliminação da equipe.

### Exemplos

| **Entrada** | **Saída**    |
|-------------|--------------|
| A B         | classificado |
| B B         | eliminado    |
| A N         | eliminado    |
***
## Continha

O semestre já começou e as aulas já estão ai. Você que não é bobo(a), nem nada, decidiu treinar programação com os melhores professores da UFBA. E para mostrar seus conhecimentos,
foi requisitado que você faça um programa para resolver a expressão matemática, dada por **((A + B) * (C - D) * (E + F)) / 2** e mostre para todos que você é fera nas continhas.

### Entrada

A entrada contém 6 valores inteiros: **A, B, C, D, E, F (0 <= A, B, C, D, E, F <= 100)**

### Saída

Imprima a mensagem “Eu sou FERA nas continhas e o resultado é ”, sem as aspas, em seguida o resultado da expressão, que é um número real com uma casa decimal de precisão

### Exemplos 

| **Entrada** | **Saída** |
|:------------|:----------|
|7, 3, 15, 30, 0, 2| Eu sou FERA nas continhas e o resultado é -150.0|
|1, 2, 10, 5, 2, 2| Eu sou FERA nas continhas e o resultado é 30.0|
***
## Desenhista 

Mário cansou de pular em cogumelos, tubulações e realizar saltos em pirâmides. A idade chegou e agora ele está aposentado, e no seu tempo livre, ele adora desenhar. Dessa vez ele está praticando desenhar  pirâmides, lembrando dos velhos tempos. Ajude-o imprimindo os blocos dessa pirâmide.

### Entrada 

A entrada consiste em um número inteiro ‘P’ (1 <= P <= 20), que representa a altura que a pirâmide terá.

### Saída

Na saída você deverá imprimir a pirâmide com o caractere ‘#’, conforme a quantidade de linhas solicitadas, e nos locais vagos, usar o caracter ‘>’, como no exemplo abaixo.

### Exemplos 

| **Entrada** | **Saída** |
|:------------|:----------|
|7            |>>>>>>#<br>>>>>>##<br>>>>>###<br>>>>####<br>>>#####<br>>######<br>#######|
***
## Incursão da Divisão de Reconhecimento

A Divisão de Reconhecimento se prepara para mais uma incursão além das muralhas em uma região de interesse infestada de titãs. Como em toda boa incursão, a preparação é algo vital para o sucesso e controle de eventuais baixas. Para isso o comandante Erwin Smith te incumbiu do processo de alocação de tropas, considerando a quantidade de inimigos na região e o tempo máximo de exposição das tropas.

Sabendo que o tempo máximo de exposição das tropas nessa missão é de 1 hora e que Levi Ackerman também foi alocado para a incursão, implemente um programa que dado um número inteiro X de titãs, faz uma alocação de um número inteiro Y de tropas que deverão acompanhar Levi.

**Considere as seguintes estatísticas:**
(Levi Ackerman -> Mata 20 titãs por hora)
(Soldado comum -> Mata 5 titãs por hora)

### Entrada

A entrada possui **um único número inteiro ‘N’ (20 ≤ N ≤ 200)**, que representa a **quantidade de titãs na região**, e **será sempre um múltiplo de 5**.

### Saída

A saída consiste em um **número inteiro X** que representa **a quantidade de soldados comuns necessários para eliminar <u>todos</u> os titãs durante 1 hora de missão**

### Exemplos

| **Entrada** | **Saída** |
|:------------|:----------|
|100| 16|
|30|2|
|20|0|

## Drone da Amazônia

A loja virtual e mundialmente famosa Amazônia decidiu fazer suas
entregas utilizando drones. Porém, ainda é necessário implementar a parte do código que irá dizer ao drone se ele está na coordenada determinada para a entrega ou não. Você deve escrever um programa que dadas as coordenadas para a entrega e as coordenadas atuais do drone, diga se o drone pode ou não soltar o pacote.

### Entrada

A primeira linha da entrada consiste de dois inteiros, X1 e Y1, que correspondem às coordenadas para a entrega. A segunda linha consiste de dois inteiros, X2 e Y2, correspondentes às coordenadas atuais do drone. Saiba que 1 <= X1, Y1, X2, Y2 <= 1000.

### Saída 

Seu programa deve imprimir em uma única linha “Soltar pacote” (sem aspas), caso as coordenadas da entrega e do drone sejam iguais, ou “Nao soltar pacote” (sem aspas e sem til), caso as coordenadas sejam diferentes.

### Exemplos

| **Entrada** | **Saída** |
|:------------|:----------|
|5 20 5 20|Soltar pacote|
|3 4 2 4| Nao soltar pacote|

## Média Ponderada

Em uma disciplina da UFBA, as notas dos alunos são compostas por 3 avaliações: duas provas online com peso 4 e um trabalho final com peso 2. Sabendo disso, escreva um programa que leia as notas dos alunos e calcule a média ponderada das notas.

### Entrada

A entrada contém uma linha com três números decimais, representando as notas das duas provas e do trabalho final, respectivamente.

### Saída 

Imprima a média ponderada das notas do aluno com duas casas decimais após a vírgula.

### Exemplos

| **Entrada** | **Saída** |
|:-----------|:-----------|
|8.0 7.5 9.0|8.00|
|6.5 6.0 6.5|6.30|
|5.0 10.0 8.0|7.60|
