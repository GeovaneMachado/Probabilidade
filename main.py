print("Seja Bem vindo!")
menu1=int(input("Digite 1 para Probabilidade Binomial individual\nDigite 2 para Probabilidade Binomial Acumulada\n = "))
while True:
    if menu1 != 1 and menu1 != 2:
        print("Opção invalida!")
        menu1=int(input("Digite 1 para Probabilidade Binomial individual\nDigite 2 para Probabilidade Binomial Acumulada\n = "))
    else:
        break

