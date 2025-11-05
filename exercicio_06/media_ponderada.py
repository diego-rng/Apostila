print("-------------------------")
print("     Média Ponderada     ")
print("-------------------------")
print("")
print("A entrada contém uma linha com três números decimais, representando as notas das duas provas e do trabalho final, respectivamente.")
print("")
print("Imprima a média ponderada das notas do aluno com duas casas decimais após a vírgula.")
print("-------------------------")

n1, n2, tf = input("Insira as notas das duas provas e trabalho final (nessa ordem): ").split()

n1 = float(n1)
n2 = float(n2)
tf = float(tf)

med = (n1*4 + n2 * 4 + tf * 2) / (4 + 4 + 2)

print (f"Sua média é {med:.2f}")
