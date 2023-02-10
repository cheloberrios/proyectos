#1
def a():
    return 5
print(a())

#saldra un 5

#2
def a():
    return 5
print(a()+a())

#sale un 10 


#3
def a():
    return 5
    return 10
print(a())

# sale un 5 por que el primer return termina la funcion

#4
def a():
    return 5
    print(10)
print(a())

#sale un 5 

#5
def a():
    print(5)
x = a()
print(x)

# no sale nada pq a no tiene valor 

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

# deberia dar un error por que no se define dentro de la funcion el valor de a

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#debiese arrojar un 100 y luego un 10, pero el primer return debiese terminar la funcion. 

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#Debiese mostrar un 7, luego un 14 luego un 21 

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

# debiese mostrar un 8 

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#muestra un 500 luego un 500 luego un 300 dps un 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)

# igual que el anterior 

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#500,500,300,300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

# 1,3,2,3,2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#1,5,3,10
