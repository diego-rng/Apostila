print("----------------------------")
print("     Inventário Caótico     ")
print("----------------------------")
print("")
print("A entrada cosistirá de várias linhas, onde em cada uma teremos uma string representando o nome de determinado item. A entrada com o nome dos itens termina quando for digitado a palavra 'fim'. Por fim, será dado o nome do item que Jônatas quer saber se está no inventário dele.")
print("")
print("Deverá ser impresso 'item encontrado' caso o item esteja no inventário ou 'voce ainda nao descobriu este item', caso contrário.")
print("----------------------------")
print("")

inv = []

for h in range(1000):
    item = str(input())
    if item == "fim": break
    else: inv.append(item)

needItem = input("")

for i in range(len(inv)):
    if inv[i] == needItem:
        print("item encontrado")
        quit()
        
print("voce ainda nao descobriu esse item")
