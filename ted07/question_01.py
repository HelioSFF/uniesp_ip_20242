'''Contexto: Crie um programa que peça ao usuário para inserir várias
 notas de um aluno e calcule a média. Utilize um loop para continuar
pedindo notas até que o usuário digite um valor específico para encerrar a entrada 
(por exemplo, -1).'''

def media(*args):
    media = 0
    count = 0
    for i in args:
        media += i
        count += 1
    
    result = media/count
    print(f'A media é igual a {result}')

if __name__ == '__main__':
    print('starting program...')
    notes = []
    tic = 0
    while tic != -1:
        notamedia = float(input('Digite a nota: '))
        if notamedia >= 0:
            notes.append(notamedia)
            average = media(*notes)
            tic = int(input(f'Deseja adicionar mais notas? \n digite 0 para continuar \n e -1 para finalizar o programa:  '))
        else:
            print('Nota inválida, por favor digite uma nota positiva.')
    print('finishing program...')