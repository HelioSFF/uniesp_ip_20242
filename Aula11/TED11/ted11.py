'''Faça um algoritmo para ler 10 números e armazenar em um vetor VET, verificar e escrever se existem
números repetidos no vetor VET e em que posições se encontram.'''

def add_number(*args):
    lista = list(args)    
    duplicates = {}
    
    for index, numeros in enumerate(lista):
        if lista.count(numeros) > 1:  
            if numeros not in duplicates:
                duplicates[numeros] = [] 
            duplicates[numeros].append(index) 
    
    if duplicates:
        print("Numeros repetidos e suas posições:")
        for numeros, posicao in duplicates.items():
            print(f"Numero {numeros} encontrado nas posições: {posicao}")
    else:
        print("Sem numeros repetidos.")
    
    print("Lista sem duplicatas:", set(lista))
   

    

if __name__ == '__main__':
    print('---------------------------------Starting program----------------------')
    add_number(5,4,3,10,23,10,11,6,7,8)
    print('--------------------------------Finishing program----------------------')
