import funcoes
print("Seja Bem vindo!")
menu1=funcoes.menu()
if menu1 == 1:
    x=float(input("Digite um valor para atribuir a X: "))
    p=float(input("Digite um valor absoluto para atribuir a P: "))
    n=float(input("Digite um valor para atribuir a N: "))
    fracasso = (1 - p)
    combinacao=funcoes.comb(n,x)
    proba=combinacao*((p**x)*(fracasso**(n-x)))
    print(proba)
else:
    x=float(input("Digite um valor para atribuir a X: "))
    p=float(input("Digite um valor absoluto para atribuir a P: "))
    n=float(input("Digite um valor para atribuir a N: "))
