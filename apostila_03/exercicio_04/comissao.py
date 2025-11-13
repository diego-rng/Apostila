print("------------------")
print("     Comissão     ")
print("------------------")
print("")
print("Receber o nome do vendedor, seu salário fixo e o total de vendas efetuadas no mês")
print("")
print("Imprimir o nome, salário fixo e o salário no final do mês")
print("------------------")
print("")

nome, sal, vend = input().split()
sal = int(sal); vend = int(vend)

finSal = int(sal + (vend * 0.15))

print(f"{nome}, {sal}, {finSal}")

