print("------------------------")
print("     Fazendo um Gol     ")
print("------------------------")
print("")
print("A entrada é composta por apenas duas linhas contendo dois caracteres em cada. Na primeira linha temos 'z' e 'g', sendo 'z' a direção que o zagueiro irá para tentar bloquear o drible do atacante e 'g' a direção que o goleiro irá tentar defender o chute do atacante. A segunda linha contém dois caracteres 'd' e 'c', que são respectivamente, a direção que o atacante irá tentar driblar o zagueiro, e se passar pelo zagueiro, a direção que o atacante irá chutar para o gol. Saiba que os valores possíveis para 'z', 'g', 'd' e 'c' são esquerda ou direita, representados pelos caracteres 'e' e 'd', respectivamente.")
print("")
print("A saída depende das seguintes situações: 1) no caso do zagueiro e atacante irem na mesma direção, só haverá uma linha na saída e ve-se imprimir a frase 'Bloqueado'; 2) no caso de zagueiro e atacante irem em direções opostas, a frase impressa na primeira linha será 'Driblado'; 3) caso o atacante tenha passado pelo zagueiro e o atacante chute na mesma direção que o goleiro foi para tentar defender, a frase impressa na segunda linha será '...e o goleiro pega'; 4) caso o atacante chute para um lado e goleiro vá para o outro a frase na segunda linha será 'Gol'.")
print("------------------------")
print("")

while True:
    zag, gol = input("Insira a direção que o zagueiro foi para bloquear e a direção que o goleiro foi para defender, respectivamente. ").split()
    print("")
    
    match zag:
        case "d":
            break
        case "e": 
            break
        case _:
            print("Insira direções corretas.")
            print("")
            continue
    
    match gol: 
        case "d": 
            break
        case "e":
            break
        case _:
            print("Insira direções corretas.")
            print("")
            continue

while True:
    dir, chu = input("Insira a direção que o atacante vai tentar driblar o zagueiro e a direção que vai tentar chutar se driblar, respectivamente. ").split()
    print("")
    
    match dir:
        case "e":
            break
        case "d":
            break
        case _:
            print("Insira direções corretas.")
            print("")
            continue
    
    match chu:
        case "e":
            break
        case "d":
            break
        case _:
            print("Insira direções corretas.")
            print("")
            continue
lin2 = None
if zag != dir:
    lin1 = "Bloqueado"
else:
    lin1 = "Driblado"

if zag == dir:
    if chu != gol:
        lin2 = "...e o goleiro pega"
    else: 
        lin2 = "Gol"

if lin2:
    print(lin1)
    print(lin2)
else: 
    print(lin1)
    