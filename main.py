print("Seja Bem vindo!")
menu1=int(input("Digite 1 para Probabilidade Binomial individual\nDigite 2 para Probabilidade Binomial Acumulada\n = "))
while True:
    if menu1 != 1 and menu1 != 2:
        print("Opção invalida!")
        menu1=int(input("Digite 1 para Probabilidade Binomial individual\nDigite 2 para Probabilidade Binomial Acumulada\n = "))
    else:
        break
if menu1 == 1:
    x=float(input("Digite um valor para atribuir a X: "))
    p=float(input("Digite um valor absoluto para atribuir a P: "))
    n=float(input("Digite um valor para atribuir a N: "))
else:
    x=float(input("Digite um valor para atribuir a X: "))
    p=float(input("Digite um valor absoluto para atribuir a P: "))
    n=float(input("Digite um valor para atribuir a N: "))
