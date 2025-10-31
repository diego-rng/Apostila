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
    6. [Exercício 6 - Média Ponderada](#média-ponderada)
    7. [Exercício 7 - Contador de Segundos](#contador-de-segundos)
    8. [Exercício 8 - Escolha do Campeão](#escolha-do-campeão)
    9. [Exercício 9 - Contabilizando Pokémons](#contabilizando-pokémons)
    10. [Exercício 10 - Fazendo um gol](#fazendo-um-gol)
    11. [Exercício 11 - Super Mario Bros](#super-mario-bros)
    12. [Exercício 12 - As Novas Missões Jedi](#as-novas-missões-jedi)
    13. [Exercício 13 - Bolinhas de Gude](#bolinhas-de-gude)



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
***
## Drone da Amazônia

A loja virtual e mundialmente famosa Amazônia decidiu fazer suas
entregas utilizando drones. Porém, ainda é necessário implementar a parte do código que irá dizer ao drone se ele está na coordenada determinada para a entrega ou não. Você deve escrever um programa que dadas as coordenadas para a entrega e as coordenadas atuais do drone, diga se o drone pode ou não soltar o pacote.

### Entrada

A primeira linha da entrada consiste de dois inteiros, **X1** e **Y1**, que correspondem às coordenadas para a entrega. A segunda linha consiste de dois inteiros, **X2** e **Y2**, correspondentes às coordenadas atuais do drone. Saiba que **1 <= X1, Y1, X2, Y2 <= 1000**.

### Saída 

Seu programa deve imprimir em uma única linha "**Soltar pacote**" (sem aspas), caso as coordenadas da entrega e do drone sejam iguais, ou "**Nao soltar pacote**" (sem aspas e sem til), caso as coordenadas sejam diferentes.

### Exemplos

| **Entrada** | **Saída** |
|:------------|:----------|
|5 20 5 20|Soltar pacote|
|3 4 2 4| Nao soltar pacote|
***
## Média Ponderada

Em uma disciplina da UFBA, as notas dos alunos são compostas por 3 avaliações: duas provas online com peso 4 e um trabalho final com peso 2. Sabendo disso, escreva um programa que leia as notas dos alunos e calcule a média ponderada das notas.

### Entrada

A entrada contém uma linha com três números decimais, representando as notas das duas provas e do trabalho final, respectivamente.

### Saída 

Imprima a média ponderada das notas do aluno **com duas casas decimais** após a vírgula.

### Exemplos

| **Entrada** | **Saída** |
|:-----------|:-----------|
|8.0 7.5 9.0|8.00|
|6.5 6.0 6.5|6.30|
|5.0 10.0 8.0|7.60|
***
## Contador de segundos

Senku é um garoto muito inteligente e gosta de contar o tempo em segundos. As vezes, quando precisa contar um tempo muito longo, ele pode se perder e errar a conta. Senku quer saber se contou o tempo de um determinado evento em segundos corretamente, para isso ele precisa que você converta o tempo em segundos, que ele calculou, para horas, minutos e segundos.

### Entrada

Será dado um número inteiro **N (1 <= N <= 100000000)** que representa o tempo do evento em segundos.

### Saída

Contém o tempo dado em segundos convertido para horas, minutos e segundos, como nos exemplos abaixo.

### Exemplos

| **Entrada** | **Saída** |
|:------------|:----------|
|4000|1h 6m 40s|
|5200|1h 26m 40s|
|59|0h 0m 59s|

***
## Escolha do Campeão

League of Legends está cheio de campeões de vários tipos, de mentes malignas a monstros épicos. Diferentes campeões assumem diferentes papéis e usam diferentes estratégias. Lucas sempre joga LOL e gosta de variar na sua escolha de campeão, **dessa vez ele quer jogar com o campeão de maior nível de poder** dentre os que ele mais gosta.

**Dado um número ‘N’, que representa a quantidade de campeões favoritos de Lucas, ajude ele a decidir qual deles tem o maior nível.**

### Entrada

A entrada consiste na primeira linha de um número inteiro **'N' (1 < N < 100)** que representa **o número de campeões favoritos de Lucas**. Nas próximas **'N'** linhas será fornecido em cada uma, um número inteiro **'P' (0 <= P <= 10000)** que representa **o nível de poder de cada um dos 'N' campeões.**

### Saída

A saída deverá **conter apenas o nível de poder do campeão mais forte**.

### Exemplos 

| **Entrada** | **Saída** |
|:------------|:----------|
|3 1500 3600 500|3600|
|7 300 5200 540 729 3567 480 4000|5200|

***
## Contabilizando Pokémons

A Pokédex, também conhecida como Poké-
Agenda, é uma enciclopédia virtual portátil de alta tecnologia que os treinadores Pokémon transportam para registrar todas as espécies diferentes de Pokémon que são encontradas durante a sua viagem como treinadores.

O novo modelo de Pokédex está sendo
desenvolvido e registra monstrinhos das regiões de Kanto, Johto e Hoenn. Sempre que Pokémons de uma nova espécie são capturados, a Pokédex deve adicionar a quantidade de Pokémons capturados ao contador das regiões em que eles são originários. Sua missão é desenvolver um programa que implemente essa funcionalidade

### Entrada

A entrada é composta de 2 linhas. A primeira linha contém três inteiros que representam o número de pokémons já registrados na Pokédex de cada região, na ordem 'K' (Kanto), 'J' (Johto) e 'H' (Hoenn). A segunda linha contém o número de novos pokémons capturados de cada região na mesma ordem da primeira linha. 

> Restrições:
>> (0 <= K,J,H <= 100)

### Saída

Imprima, na ordem da entrada (K J H), o número total de pokémons de cada região após a nova contagem, separados por espaço. Imprima uma quebra de linha no fim.

### Exemplos

| **Entrada** | **Saída** |
|:------------|:----------|
|92 40 54 1 0 0| 93 40 54 |
|12 1 0 0 2 2 | 12 3 2    |

***
## Fazendo um gol

O jogo favorito de Lucas é Bomba Patch. Atualmente, ele está desenvolvendo uma forma de saber qual é o melhor lado para driblar o zagueiro adversário e chutar para o gol. Por isso ele pediu sua ajuda para desenvolver um programa que vai receber as direções que o zagueiro e o goleiro tentarão defender, e as direções que o atacante irá tentar driblar o zagueiro e chutar para gol, e diga se o atacante terá sucesso ou não.

### Entrada 

A entrada é composta por apenas duas linhas contendo dois caracteres em cada. Na primeira linha temos "z" e "g", sendo "z" a direção que o zagueiro irá para tentar bloquear o drible do atacante e "g" a direção que o goleiro irá tentar defender o chute do atacante. A segunda linha contém dois caracteres "d" e "c", que são respectivamente, a direção que o atacante irá tentar driblar o zagueiro, e se passar pelo zagueiro, a direção que o atacante irá chutar para o gol. Saiba que os valores possíveis para “z”, ”g”, “d” e “c” são esquerda ou direita, representados pelos caracteres ‘e’ e ‘d’, respectivamente.

### Saída

A saída depende das seguintes situações: 1) no caso do zagueiro e atacante irem na mesma direção, só haverá uma linha na saída e ve-se imprimir a frase "Bloqueado"; 2) no caso de zagueiro e atacante irem em direções opostas, a frase impressa na primeira linha será "Driblado"; 3) caso o atacante tenha passado pelo zagueiro e o atacante chute na mesma direção que o goleiro foi para tentar defender, a frase impressa na segunda linha será "...e o goleiro pega"; 4) caso o atacante chute para um lado e goleiro vá para o outro a frase na segunda linha será "Gol".

Obs.: **Só há a segunda linha na saída se o atacante passar pelo zagueiro. Sempre
interprete os dados na perspectiva dos próprios jogadores, ou seja, para qual lado cada um vai.**

### Exemplos

| **Entrada** | **Saída** |
|:------------|:----------|
|e e e d      | Driblado ...e o goleiro pega|
|d d d d      | Driblado Gol|
|e d d d      | Bloqueado |

***
## Super Mario Bros

No New Super Mario Bros você entra no Mushroom Kingdom, e persegue o Bowser Jr. e a princesa Peach que foi raptada! Você precisa explorar oito mundos para encontrar todas as 240 Star Coins. Para isto, é preciso pôr em prática as tuas habilidades e usar ajudas adicionais como o Mega Mushroom, a Carapaça Koopa Azul e o Mini Mushroom para que nada fique por descobrir. **Em um determinado mundo, sabe-se que temos 3 áreas secretas, onde é possível encontrar em cada uma, 10 Star Coins, 2 Mega Mushrooms e 1 Carapaça Koopa Azul. Para ir ao próximo mundo você deve encontrar todas as Star Coins deste mundo**.

### Entrada 

Considerando as três áreas secretas, a entrada **consiste nos itens que você conseguiu encontrar**, sendo três números inteiros **'SC' (0 <= SC <= 30), 'MM' (0 <= MM <= 6)** e **'CK' (0 <= CK <= 3)** representando, respectivamente, **Star Coins, Mega Mushrooms e Carapaças Koopa Azul**.

### Saída 

A saída consiste em uma única linha. Caso você não tenha encontrado todas as Star Coins, **deve ser impresso a quantidade de itens ainda por serem descobertos no mundo atual, sendo impresso primeiro a quantidade de Star Coins, seguido pela quantidade de Mega Mushrooms e por fim, a quantidade de Carapaças Koopa Azul**. Caso você tenha conseguido encontrar todas as Star Coins você deve imprimir a mensagem "**PROXIMO MUNDO**".

### Exemplos

| **Entrada** | **Saída** |
|:------------|:----------|
|30 1 2       |PROXIMO MUNDO|
|3 1 0        |27 5 3     |
|10 4 0       |20 2 3     |

***
## As Novas Missões Jedi

Há muito tempo atrás em uma galáxia muito muito distante, por mais de mil gerações, os Cavaleiros Jedi foram os guardiões da paz e da justiça na Velha República. A Ordem Jedi era uma ordem hierárquica indo desde Jedi Iniciado, Jedi Padawan, até o Grande Mestre, sendo Yoda um exemplo.

Para permitir um bom aprendizado dos poderes, várias missões eram realizadas, **aumentando o XP do Jedi em ‘X’ pontos caso este cumprisse a missão**. Assim, várias missões serão atribuídas aos Jedi e você foi escolhido para ajudar. Lembre-se que a força está com você, Padawan.

### Entrada

Seu programa receberá primeiramente um inteiro **'N' (1 ≤ 'N' ≤ 100)** e um inteiro **'XP' (1 ≤ 'XP' ≤ 100)**, que representam respectivamente, a quantidade de missões a serem realizadas igualmente por Yoda, Luke e Ahsoka, seguido da quantidade de XP que estes ganharão ao completar cada missão. Na linha seguinte serão dados **3 inteiros** que representam os respectivos níveis iniciais de XP **'XPi' (1 <= 'XPi' <= 1500)** de Yoda, Luke e Ahsoka.

### Saída 

**Para cada** Jedi, **Yoda, Luke e Ahsoka**, nessa ordem, você **deverá imprimir uma linha com seu nome e seu novo 'XP'**, separados por espaço. Portanto, assuma que eles já cumpriram todas as novas missões ao imprimir seus dados

### Exemplos

| **Entrada** | **Saída** |
|:------------|:----------|
|3 50 --- 1500 800 1000|Yoda 1650 Luke 950 Ahsoka 1150|
|5 1 --- 5 2 4|Yoda 10 Luke 7 Ahsoka 9|

*** 
## Bolinhas de Gude

O natal está chegando e Yuri já deixou avisado a seus familiares que gostaria de receber bolinhas de gude como presente este ano. Yuri sabe que seus familiares têm um hábito peculiar quando o assunto é presentear com bolinhas de gude, pois sempre que um familiar lhe presenteia com uma quantidade de bolinhas de gude o próximo familiar presenteia com o dobro do anterior. Como Yuri sabe que você é um ótimo programador, ele pediu para que você desenvolva um programa que dada a quantidade de familiares que irá presenteá-lo com bolinhas de gude e a quantidade de bolinhas de gude que o primeiro familiar lhe dará, informe a quantidade total de bolinhas de gude que ele irá receber de presente de natal.

### Entrada

A entrada é composta por um número inteiro **N (1 ≤ N ≤ 50)**, que representa a quantidade de familiares que irão presenteá-lo com bolinhas de gude e um inteiro **Q (1 ≤ N ≤ 50)**, que representa a quantidade de bolinhas que o primeiro familiar dará de presente.

### Saída

A saída consiste em imprimir a quantidade total de bolinhas de gude que Yuri irá receber.

### Exemplos 

| **Entrada** | **Saída** |
|:------------|:----------|
|10 2         |2046       |
|5 15         |465        |

***