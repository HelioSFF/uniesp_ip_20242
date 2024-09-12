apples = int((input("Insira quantidades de maças: ")))
if apples > 11:
    compra = apples * 1
    print(f'Você comprou total de {apples} maças e o preço da compra foi {compra} R$')
else:
    compra = apples * 1.30
    print(f'Você comprou total de {apples} maças e o preço da compra foi {compra} R$')