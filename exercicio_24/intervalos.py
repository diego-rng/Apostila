print("--------------------")
print("     Intervalos     ")
print("--------------------")
print("")
print("A entrada contém três linhas: a primeira corresponde ao primeiro intervalo (]x,y]); a segunda corresponde ao segundo intervalo ([w,z[); e a terceira corresponde ao número inteiro que se quer descobrir o intervalo ao qual pertence.")
print("")
print("A saída deve ser conforme exemplos na apostila.")
print("--------------------")
print("")

while True:
    inter11, inter12 = input("Insira o primeiro intervalo: ").split()
    print("")
    inter11 = int(inter11)
    inter12 = int(inter12)
    if inter11 < inter12:
        break
    else: 
        print("Insira um intervalo válido!")
        print("")
        continue

while True:
    inter21, inter22 = input("Insira o segundo intervalo: ").split()
    print("")
    inter21 = int(inter21)
    inter22 = int(inter22)
    if inter21 < inter22:
        break
    else: 
        print("Insira um intervalo válido!")
        print("")
        continue
        
num = int(input("Insira o número que quer validar: "))
print("")

def intervalCheck(var1 = int, var2 = int, var3 = int, var4 = int, var5 = int):
    apply = []
    check1 = var1 < var5 <= var2
    check2 = var3 <= var5 < var4
    if check1:
        apply.append(1)
    else: 
        apply.append(0)
    if check2:
        apply.append(1)
    else:   
        apply.append(0)
    
    return apply

match intervalCheck(inter11, inter12, inter21, inter22, num):
    case [1, 0]:
        print("Primeiro intervalo!")
    case [0, 1]:
        print("Segundo intervalo!")
    case [1, 1]:
        print("Ambos!")
    case _:
        print("Nenhum!")
