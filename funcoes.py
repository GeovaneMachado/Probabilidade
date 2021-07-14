def comb(x,y):
    import math
    fatx = math.factorial(x)
    faty = math.factorial(y)
    fatyx = math.factorial(x-y)
    combinacao = fatx / (fatyx * faty)
    return combinacao


def menu():
    menu1=int(input("Digite 1 para Probabilidade Binomial individual\nDigite 2 para Probabilidade Binomial Acumulada\n = "))
    while True:
        if menu1 != 1 and menu1 != 2:
            print("Opção invalida!")
            menu1=int(input("Digite 1 para Probabilidade Binomial individual\nDigite 2 para Probabilidade Binomial Acumulada\n = "))
        else:
            break
    return menu1

'''a=int(input("N: "))
c=int(input("N: "))
b=comb(a,c)
print(b)'''