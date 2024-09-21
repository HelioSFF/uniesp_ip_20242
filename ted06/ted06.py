import time
def send_invites(arq):
    with open (arq, "r") as arquivo:
        lines = arquivo.readlines()
        for i in lines:
            print(f'{i.strip()}! You have been invited for a party at my house!')
            time.sleep(1)


if __name__ == "__main__":
    print('starting program...')
    send_invites('vingadores.txt')
    print('finishing program...')   