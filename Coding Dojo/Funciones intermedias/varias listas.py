dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(lista):
    for valor in lista.values():
        print(len(valor), lista.keys())
        if isinstance(valor, list):  # Verificamos si el valor es una lista
            for elemento in valor:  # Iteramos sobre cada elemento de la lista
                print(elemento)


printInfo(dojo)
