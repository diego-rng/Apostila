print("------------------------------------")
print("     EXAME CHUNIN - EXERCÍCIO 1")
print("------------------------------------")
print("")
print("A entrada é composta por dois caracteres “P1” e “P2”, dados em linhas diferentes e representando a característica de cada pergaminho. Portanto, “P1” e “P2” podem ser “A” (azul), “B” (branco) e “N” (sem pergaminho).")
print("")
print("A saída será composta pela mensagem “classificado”, indicando que o trio foi classificado (dois pergaminhos distintos) ou “eliminado” (pergaminhos iguais ou pelo menos um pergaminho faltando), indicando a eliminação da equipe.")
print("------------------------------------")
while True: 
    p1 = input("P1: ")
    match p1:
        case "A": 
            print("")
            break
        case "B": 
            print("")
            break
        case "N":
            print("") 
            break
        case _: 
            print("Escreva um tipo de pergaminho correto!")
            print("")
            continue
        
while True:
    p2 = input("P2: ")
    match p2:
        case "A": 
            print("")
            break
        case "B": 
            print("")
            break
        case "N": 
            print("")
            break
        case _: 
            print("Escreva um tipo de pergaminho correto!")
            print("")
            continue

if p1 == "B" and p2 == "B": 
    print("eliminado")
elif p1 == "A" and p2 == "N": 
    print("eliminado")
elif p1 == "N" and p2 == "A": 
    print("eliminado")
elif p1 == "A" and p2 == "B":
    print("classificado")
elif p1 == "B" and p2 == "A":
    print("classificado")