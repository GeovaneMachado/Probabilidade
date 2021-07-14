import funcoes
print("Seja Bem vindo!")
menu1=funcoes.menu() 
if menu1 == 1:
    x=float(input("Digite um valor para atribuir a X: "))
    p=float(input("Digite um valor absoluto para atribuir a P: "))
    n=float(input("Digite um valor para atribuir a N: "))
    fracasso = (1 - p)  # probabilidade de fracasso
    combinacao=funcoes.comb(n,x) # Chama a função que calcula a combinação de n elementos tomados x a x 
    proba=combinacao*((p**x)*(fracasso**(n-x))) # calcula a probabilidade binomial individual
    print(proba)
else:
    x=float(input("Digite um valor para atribuir a X: "))
    p=float(input("Digite um valor absoluto para atribuir a P: "))
    n=float(input("Digite um valor para atribuir a N: "))
