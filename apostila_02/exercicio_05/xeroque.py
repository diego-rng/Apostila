print("------------------------")
print("     Xeroque Rolmes     ")
print("------------------------")
print("")
print("A entrada é composta por 6 linhas, cada linha contém uma palavra encontrada.")
print("")
print("A saída é composta por uma linha com a senha do cofre.")
print("------------------------")
print("")

passList = []

for i in range(6):
    words = str(input(f"Insira a {i+1}ª palavra: "))
    passList.append(words)

num1 = len(passList.pop(0)) 
num2 = len(passList.pop(0))
num3 = len(passList.pop(0))
num4 = len(passList.pop(0))
num5 = len(passList.pop(0))
num6 = len(passList.pop(0))

print(f"{num1}{num2}{num3}{num4}{num5}{num6}")

