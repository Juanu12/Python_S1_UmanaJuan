

def editrest (b,c,d,e,f):
    b[c-1]=d
    e[c-1]=f

def lista (a,b):
    for i in range (len(a)):
        print("Estudiante","#", i +1," ".join(a[i]), " ".join(b[i]))

def ag (a,b,c,d):
    a.append (b)
    c.append (d)

def el (a,b,c):
    del a [b-1]
    del c [b-1]

def fin ():
    exit
