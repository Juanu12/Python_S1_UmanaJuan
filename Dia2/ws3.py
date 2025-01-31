def paroImpar(a):
    if  a% 2 ==0:
        print( a, "El numero es par")
    else: print (a, "El numero es impar")

def primooCompuesto (b):
    if b/2 == int or b/3 == int:
        print(b, "El numero es primo")
    else:
        print(b, "El numero es compuesto" )

def cuadradoPerfecto (c):
    num = int (c**0.5)
    if num*num == c:
        print(c, "Es un cuadrado perfecto")
    else:
        print(c, "no es un cuadrado perfecto")

n=int (input("Ingrese el numero"))
print(paroImpar(n))
print(primooCompuesto(n))
print(cuadradoPerfecto(n))

