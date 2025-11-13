print("---------------")
print("     Média     ")
print("---------------")
print("")
print("Receber o nome do aluno e as notas das 3 provas que recebeu esse semestre.")
print("")
print("Imprimir o nome do aluno e sua média (aritmética).")
print("------------------")
print("")

nome, A1, A2, A3 = input().split()

nome = str(nome); A1 = int(A1); A2 = int(A2); A3 = int(A3)

med = ((A1 + A2 + A3)/3)

print(f"{nome}, Média {med:.1f}")