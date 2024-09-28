'''Contexto: Crie um programa que peça ao usuário um número inteiro e verifique se ele é primo. 
Utilize um loop para testar a divisibilidade do número por outros números menores.'''

def primo(number):
    if number < 0:
        return False
    else:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                return False
        return True

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    while n >= 0:
        if primo(n):
            print(f"{n} is a prime number.")
            n = int(input("Enter a number:    (Type)"))
        else:
            print(f"{n} is not a prime number.")
            n = int(input("Enter a number: "))
        
    