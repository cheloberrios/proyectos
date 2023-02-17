#Dada una lista de números, crea una función para reemplazar el último valor con el número de valores positivos.
# (Ten en cuenta que el 0 no se considera un número positivo).
#Ejemplo: count_positives([-1,1,1,1]) cambia la lista original a[-1,1,1,3] y la devuelve
#Ejemplo: count_positives([1,6,-4,-2,-7,-2]) cambia la lista original a [1,6,-4,-2,-7,2] y la devuelve

def count(lista):
    conteo = 0 
    for i in range(len(lista)):
        if i >0:
            conteo = conteo + 1
    lista[-1] = conteo  
    print(lista)
    print(count)
        

lista = [-1,1,1,1]

count(lista)