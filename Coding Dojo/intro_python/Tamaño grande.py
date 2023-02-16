#Tamaño grande - Dada una lista, 
# escribe una función que cambie todos los números positivos de la lista a “big”.
#Ejemplo: biggie_size([-1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores ahora son [-1, "big", "big", -5]

def big_size(lista):
    lista1 = []
    for i in lista:
        if i < 0:
            lista1.append(i)
        else:
            lista1.append("big")
    print(lista1)

lista = [-1, 3, 5, -5]

big_size(lista)