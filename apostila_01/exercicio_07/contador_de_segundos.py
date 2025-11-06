print("------------------------------")
print("     Contador de Segundos     ")
print("------------------------------")
print("")
print("ENTRADA:")
print("Será dado um número inteiro N (1 <= N <= 100000000) que representa o tempo do evento em segundos.")
print("")
print("SAÍDA:")
print("Contém o tempo dado em segundos convertido para horas, minutos e segundos, como nos exemplos abaixo.")
print("------------------------------")

while True: 
    N = int(input("Insira o número de segundos: "))
    print("")
    checkValid = 1 <= N <= 100000000
    if checkValid: 
        break
    else: 
        print("Insira um número válido!")
        print("")
        continue

if N < 60:
    checkSecond = N
else: 
    checkSecond = 0
    
if 60 <= N <= 3599:
    checkMinute = int((N / 60))
    checkSecond = int(N - (checkMinute * 60))
else: 
    checkMinute = 0

if N >= 3600:
    checkHour = int((N / 3600))
    checkMinute = int(((N - (checkHour * 3600)) / 60))
    checkSecond = int((N - (checkHour * 3600) - (checkMinute * 60)))
else: 
    checkHour = 0

print(f"O número equivale a {checkHour}h {checkMinute}m {checkSecond}s")