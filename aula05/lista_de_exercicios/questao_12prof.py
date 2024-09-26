def validar_arma(ataque, durabilidade, nome_arma):
    if ataque > 50 and durabilidade > 70:
        print('Arma Validada!')
        return nome_arma
    else:
        return 'error'
    
if __name__ == '__main__':

    controle_opcao = 1000

    while controle_opcao != 1:
        nome_arma = input('Digite o nome da arma: ')
        ataque_arma = int(input('Digite o ataque da arma: '))
        durabilidade_arma = int(input('Digite a durabilidade da arma: '))

        resultado_validacao = validar_arma(ataque_arma,durabilidade_arma, nome_arma)
        