print("-----------------------------------------------")
print("     Incursão da Divisão de Reconhecimento     ")
print("-----------------------------------------------")
print("")
print("A entrada possui um único número inteiro 'N' (20 ≤ N ≤ 200), que representa a quantidade de titãs na região, e será sempre um múltiplo de 5.")
print("")
print("A saída consiste em um número inteiro X que representa a quantidade de soldados comuns necessários para eliminar todos os titãs durante 1 hora de missão.")
print("-----------------------------------------------")

while True:
    N = int(input("Quantos titãs foram reportados na área? "))
    print("")
    under = 20 > N
    over = N > 200
    if under: 
            print("Alguns soldados comuns conseguem lidar com esse tanto, volte quando houverem 20 ou mais.") 
            print("")
            continue
    if over: 
            print("Estamos perdidos.")
            print("")
            continue
    
    if under == False and over == False:
        break
    

X = int((N - 20) / 5)

print(f"Iremos precisar de {X} soldados comuns para acompanhar o Levi para eliminar todos esses titãs em uma hora.")
