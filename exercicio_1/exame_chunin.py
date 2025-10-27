from re import match
while True: 
    p1 = input("P1: ")
    match p1:
        case "A": 
            break
        case "B": 
            break
        case "N": 
            break
        case _: 
            print("Escreva um tipo de pergaminho correto!")
            continue
        
while True:
    p2 = input("P2: ")
    match p2:
        case "A": 
            break
        case "B": 
            break
        case "N": 
            break
        case _: 
            print("Escreva um tipo de pergaminho correto!")
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