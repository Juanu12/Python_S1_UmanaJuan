def interessimple (c,i,n):
   b = c*(1+i*n)
   return b
print("Interes simple")
cap=float(input("Escribe el capital inicial"))
Tasa=float(input("Tasa de interes (decimal) aplicable a cada periodo"))
Peri=float(input("Numero de periodos en que se generarán intereses (años)"))

print("El interés corresponde a",interessimple(cap,Tasa,Peri))

def interesCompuesto (c,r,p):
   com = c*(1+r)**p
   return com
print("Interes Compuesto")
cap2=float(input("Escribe el capital inicial"))
Tasa2=float(input("Tasa de interes (en decimal) aplicable a cada periodo"))
Peri2=float(input("Numero de periodos en que se generarán intereses (años)"))

print("El interés corresponde a",interesCompuesto(cap2,Tasa2,Peri2))

