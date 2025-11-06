print("----------------------------------")
print("     DESENHISTA - EXERCÍCIO 3")
print("----------------------------------")
print("")
print("A entrada consiste em um número inteiro ‘P’ (1 <= P <= 20), que representa a altura que a pirâmide terá")
print("")
print("Na saída você deverá imprimir a pirâmide com o caractere ‘#’, conforme a quantidade de linhas solicitadas, e nos locais vagos, usar o caracter ‘>’, como no exemplo abaixo.")
print("----------------------------------")

while True:
    pirNum = int(input("Insira a altura da pirâmide: "))
    print("")
    if (1 <= pirNum <= 100):
        break
    else: 
        print("Insira uma altura entre 1 e 100.")
        print("")
        continue
         

intPirNum = pirNum
air = pirNum
pir = 0

for num in range(pirNum):
    num = 1
    while num <= pirNum:    
        print( ">" * air, "#" * pir, sep='')
        air -= 1
        pir += 1
        num += 1
    print ("#" * pir)
    break       