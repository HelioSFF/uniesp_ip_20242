'''Contexto: Desenvolva um programa que gere os primeiros N números da sequência de Fibonacci, onde N é fornecido pelo usuário. 
Utilize um loop para calcular e exibir os termos da sequência.'''

#The Fibonacci sequence follows a pattern where each number is the sum of the previous two numbers, which is why it starts with [1, 1].

def fibonacci(number):
    start = [1,1]  # The Fibonacci sequence starts with [1, 1]
    count = 2       # Start count at 1 because we already have two elements
    if number == 1:
        print('1')
    elif number == 2:
        print(start)
    elif number > 2: 
        while count < number:
        # The next number in the sequence is the sum of the last two elements
            next_value = start[-1] + start[-2]
            start.append(next_value)
            count += 1
        print(start)
    else:
        print('Error')


if __name__ == '__main__':
    print('starting program...')
    seqfibo = int(input('Digite numero para quantidade de numeros na sequencia de fibonacci: '))
    while seqfibo >= 1:
        fibonacci(seqfibo)
        seqfibo = int(input('Digite numero para quantidade de numeros na sequencia de fibonacci: (Digite 0 para terminar o programa)     '))
    print('finishing program...')
