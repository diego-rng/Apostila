print("-------------------------------")
print("     As Novas Missões Jedi     ")
print("-------------------------------")
print("")
print("Seu programa receberá primeiramente um inteiro 'N' (1 ≤ 'N' ≤ 100) e um inteiro 'XP' (1 ≤ 'XP' ≤ 100), que representam respectivamente, a quantidade de missões a serem realizadas igualmente por Yoda, Luke e Ahsoka, seguido da quantidade de XP que estes ganharão ao completar cada missão. Na linha seguinte serão dados 3 inteiros que representam os respectivos níveis iniciais de XP 'XPi' (1 <= 'XPi' <= 1500) de Yoda, Luke e Ahsoka.")
print("")
print("Para cada Jedi, Yoda, Luke e Ahsoka, nessa ordem, você deverá imprimir uma linha com seu nome e seu novo 'XP', separados por espaço. Portanto, assuma que eles já cumpriram todas as novas missões ao imprimir seus dados.")
print("-------------------------------")
print("")
while True:
    N, XP = input("Quantas missões estão agendadas para hoje? Quanta XP essas missões dão? ").split()
    N = int(N)
    XP = int(XP)    
    print("")
    if 1 <= N <= 100 and 1 <= XP <= 100:
        break
    else: 
        print("Insira um número válido!")
        print("")
        continue

while True:
    yodaXPi, lukeXPi, ahsokaXPi = input("Insira a XP inicial de Yoda, Luke e Ahsoka, respectivamente: ").split()
    yodaXPi = int(yodaXPi)
    lukeXPi = int(lukeXPi)
    ahsokaXPi = int(ahsokaXPi)
    print("")
    if 1 <= yodaXPi <= 1500 and 1 <= lukeXPi <= 1500 and 1 <= ahsokaXPi <= 1500:
        break
    else: 
        print("Insira um número válido!")
        print("")
        continue

yodaNXP = int((yodaXPi + (N * XP)))
lukeNXP = int((lukeXPi + (N * XP)))
ahsokaNXP = int((ahsokaXPi + (N * XP)))

print(f"Yoda {yodaNXP} \nLuke {lukeNXP} \nAhsoka {ahsokaNXP}")
