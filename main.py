import funcoes
print("Seja Bem vindo!")
menu1=funcoes.menu() 
if menu1 == 1:
    x=float(input("Digite o numero especificado de sucessos (x): "))
    p=float(input("Digite o valor absoluto da probabilidade de sucesso (p): "))
    n=float(input("Digite o numero de observações (n): "))
    fracasso = (1 - p)  # probabilidade de fracasso
    combinacao=funcoes.comb(n,x) # Chama a função que calcula a combinação de n elementos tomados x a x 
    proba=combinacao*((p**x)*(fracasso**(n-x))) # calcula a probabilidade binomial individual
    relativo=(proba*100)/p
    print(f"P(x={x})={relativo}")
else:
    x=float(input("Digite o numero especificado de sucessos (x): "))
    p=float(input("Digite o valor absoluto da probabilidade de sucesso (p): "))
    n=float(input("Digite o numero de observações (n): "))
    probatotal=0
    while x >= 0:
        fracasso = (1 - p)  # probabilidade de fracasso
        combinacao=funcoes.comb(n,x) # Chama a função que calcula a combinação de n elementos tomados x a x 
        proba=combinacao*((p**x)*(fracasso**(n-x))) # calcula a probabilidade binomial individual
        relativo=proba*100 #Calcula a probabilidade em valor relativo
        probatotal+=relativo #Soma as probabilidades 
        x-=1
    print(f"P(x={x})={probatotal} %")