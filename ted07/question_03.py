'''Contexto: Crie um programa que peça ao usuário uma frase e conte o número de vogais e consoantes presentes nela.
 Utilize um loop para percorrer cada caractere da frase e realizar a contagem.'''

def count_letters(frase):
    count_vowels = 0
    count_consonant = 0
    count_blank = 0
    count_numbers = 0 

    vowels = 'aeiouáéíóúãôâôîûêAEIOUÁÉÍÓÚÂÊÎÔÛÃÕ'
    consonant = 'bcdfghjklmnpqrstvwyxzçBCDFGHJKLMNPQRSTVWYYXZÇ'

    for i in frase:
        if i in vowels:
            count_vowels += 1
        elif i in consonant:
            count_consonant +=1
        elif i.isdigit():
            count_numbers += 1
        else:
            count_blank += 1
    print(f'Quantidades de vogais {count_vowels}')
    print(f'Quantidades de consoantes {count_consonant}')
    print(f'Quantidades de espaços em branco {count_blank}')
    print(f'Quantidade de digitos {count_numbers}')

if __name__ == '__main__':
    print('starting program...')
    ask = input('Digite a frase desejada:  ')
    count_letters(ask)
    print('finishing program...')
