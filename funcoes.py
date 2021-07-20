import math

def comb(x,y):
    z = x-y
    fatx = math.factorial(x)
    faty = math.factorial(y)
    fatyx = math.factorial(z)
    combinacao = fatx / (fatyx * faty)
    return combinacao


def menu():
    menu1=int(input("[1] Probabilidade Binomial individual\n[2] Probabilidade Binomial Acumulada\n = "))
    while True:
        if menu1 != 1 and menu1 != 2:
            print("Opção invalida!")
            menu1=int(input("[1] Probabilidade Binomial individual\n[2] Probabilidade Binomial Acumulada\n = "))
        else:
            break
    return menu1

def bem_vindo():
    from time import sleep
    cabe = '*=' *20
    comeco = 'Bem vindo'
    for i in cabe:
        print(i, end='')
        sleep(0.1)
    print()
    print('|             ', end='')
    for i in comeco:
        print(i, end='')
        sleep(0.1)
    print(f'{"|":>18}')
    for i in cabe:
        print(i, end='')
        sleep(0.1)
    print()


def formatar(txt):
    from time import sleep
    end = str(txt)
    for i in end:
        print(i, end='')
        sleep(0.20)
    print()
    