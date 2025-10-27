while True:
    pirNum = int(input("Insira a altura da pirâmide: "))
    if (1 <= pirNum <= 100):
        break
    else: 
        print("Insira uma altura entre 1 e 100.")
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