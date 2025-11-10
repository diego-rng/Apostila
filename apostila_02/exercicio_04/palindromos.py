print("---------------------")
print("     Palíndromos     ")
print("---------------------")
print("")
print("A primeira linha da entrada possui uma palavra S, contendo apenas letras minúsculas, a palavra dada por Luiz.")
print("")
print("A saída deve conter numa única linha a palavra “Sim”, caso S seja um palíndromo, e “Nao” caso “S” não seja um palíndromo.")
print("---------------------")
print("")

S = str(input("Insira a palavra: "))
leng = int(len(S) /2)
S1 = str(S[0:leng+1]); S2 = str(S[leng:len(S)])
palCheck = S1 == S2[::-1]

match palCheck:
    case True:
        print("Sim")
    case False:
        print("Nao")