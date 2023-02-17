#Suma total - Crea una función que tome una lista y devuelva la suma de todos los valores en el arreglo.
def total(lista):
    suma=0
    for i in lista:
        suma += i
        print(suma)
    return suma

numeros=[1,2,3,4]

total(numeros)