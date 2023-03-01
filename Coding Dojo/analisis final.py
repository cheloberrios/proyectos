#Análisis final (opcional) - 
#Crea una función que tome una lista y devuelve un diccionario que tenga 
# la sumTotal, promedio, mínimo, máximo y la longitud de la lista.
#Ejemplo: ultimate_analysis([37,2,1,-9]) debería devolver {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37,        'length': 4}

def total(lista):
    suma=0
    diccionario = {}
    for i in lista:
        suma += i
    diccionario.update({'TotalSum': suma})
    promedio = 0
    largo = len(lista)
    promedio = suma/largo
    diccionario.update({'Promedio':promedio})
    valor_max = lista[0]
    for i in lista:
        if i > valor_max:
            valor_max = i
    diccionario.update({"valor maximo": valor_max})
    valor_min = lista[0]
    for i in lista:
        if i < valor_min:
            valor_min = i
    diccionario.update({"valor minimo": valor_min})
    diccionario.update({"largo":largo})
    print(diccionario)

numeros=[1,2,3,4]

total(numeros)