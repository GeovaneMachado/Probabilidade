import funcoes
import os
funcoes.bem_vindo()
menu1=funcoes.menu()
os.system('cls') or None
x=float(input("Digite o numero especificado de sucessos (x): "))
p=float(input("Digite o valor absoluto da probabilidade de sucesso (p): "))
n=float(input("Digite o numero de observações (n): "))
if menu1 == 1:
    fracasso = (1 - p)  # probabilidade de fracasso
    combinacao=funcoes.comb(n,x) # Chama a função que calcula a combinação de n elementos tomados x a x 
    proba=combinacao*((p**x)*(fracasso**(n-x))) # calcula a probabilidade binomial individual
    relativo= proba*100
    os.system('cls') or None
    txt = f"P(x = {x}) = {relativo:.2f}%"
    funcoes.formatar(txt)
else:
    probatotal=0
    bolsa = x # guarda o valor de x para utulizar no print
    while x >= 0:
        fracasso = (1 - p)  # probabilidade de fracasso
        combinacao=funcoes.comb(n,x) # Chama a função que calcula a combinação de n elementos tomados x a x 
        proba=combinacao*((p**x)*(fracasso**(n-x))) # calcula a probabilidade binomial individual
        relativo=proba*100 #Calcula a probabilidade em valor relativo
        probatotal+=relativo #Soma as probabilidades 
        x-=1 # decrementa 1
    txt = f"P(x<={bolsa})={probatotal:.2f}%"
    funcoes.formatar(txt)
