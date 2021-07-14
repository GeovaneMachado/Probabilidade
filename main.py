def comb(x,y):
    import math
    fatx = math.factorial(x)
    faty = math.factorial(y)
    fatyx = math.factorial(x-y)
    combinacao = fatx / (fatyx * faty)
    return combinacao





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
    combinacao=comb(n,x)
    proba=combinacao*(p**x)
else:
    x=float(input("Digite um valor para atribuir a X: "))
    p=float(input("Digite um valor absoluto para atribuir a P: "))
    n=float(input("Digite um valor para atribuir a N: "))
