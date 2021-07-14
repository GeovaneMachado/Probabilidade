def comb(x,y):
    import math
    fatx = math.factorial(x)
    faty = math.factorial(y)
    fatyx = math.factorial(x-y)
    combinacao = fatx / (fatyx * faty)
    return combinacao





'''a=int(input("N: "))
c=int(input("N: "))
b=comb(a,c)
print(b)'''