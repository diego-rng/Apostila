print("----------------")
print("     Vendas     ")
print("----------------")
print("")
print("Ler o valor de custo de um produto e o percentual que a loja adiciona para vendas")
print("")
print("Imprimir o valor de venda do produto")
print("----------------")
print("")

cust, perc = input().split()

cust = float(cust); perc = float(perc)

vend = (cust + (cust * (perc/100)))

print(f"\n{vend:.2f}")