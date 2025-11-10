print("-----------------------------")
print("     Vamos jogar um jogo     ")
print("-----------------------------")
print("")
print("A primeira linha da entrada consiste de uma string S, que indica a frase a ser avaliada. A segunda linha contém um inteiro 'Q' (1 <= Q <= 30), informando a quantidade de ocorrências, seguido de uma palavra P, que indica o que deve ser detectado na frase S.")
print("")
print("Seu programa deverá imprimir a quantidade de ocorrências de P em uma linha. Na outra, deverá imprimir 'SIM!' caso essa quantidade seja igual à 'Q' e, caso contrário, deverá imprimir 'NAO!'.")
print("-----------------------------")
print("")

S = str(input())
S = S.replace(" ", "")
Q, P = input().split()

Q = int(Q); P = str(P)

times = S.count(P)

print("")

print(times)

if times == Q:
    print("SIM!")
else: 
    print("NAO!")
    