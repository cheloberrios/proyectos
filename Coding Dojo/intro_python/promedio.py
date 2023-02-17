##rea una función que tome una lista y devuelva el promedio de todos los valores.
#Ejemplo: average([1,2,3,4]) debería devolver 2.5

def promedio(lista):
    suma=0
    for i in lista:
        suma += i
        print(f'total sin promedioar', suma)
    largo = 0
    largo = largo + len(lista)
    promedio = suma / largo
    print(promedio)
    return promedio

promedio([1,2,3,4])
