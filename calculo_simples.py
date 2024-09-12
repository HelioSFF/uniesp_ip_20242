v1 = int(input('Codigo da peça: '))
v2 = int(input('Numero de peças: '))
v3 = float(input('Valor unitario: '))
print("Quer comprar mais alguma peça?")
oc = input("S/N?")
if oc == "S" or oc == "s":
    b1 = input("Codigo da peça: ")
    b2 = input("Numero de peças: ")
    b1 = int(b1)
    b2 = int(b2)
    if b1 != v1:
        b3 = input("Valor unitario: ")
        b3 = float(b3)
        resul = (v2 * v3) + (b2 * b3)
        print("VALOR A PAGAR: R$ ",resul)
    else:
        print("VALOR A PAGAR: R$ ",(v2*v3+b2*v3))
elif oc == "N" or oc == "n":
    print("VALOR A PAGAR: R$ ",v2*v3)
else:
    print("Digite S ou N")