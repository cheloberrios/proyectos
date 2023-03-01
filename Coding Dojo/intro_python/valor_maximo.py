#Crea una función que tome una lista de números y devuelva el valor mínimo en la lista.
#(Opcional) Si la lista está vacía, haz que la función devuelva False.
#Ejemplo: minimum([37,2,1,-9]) debería devolver -9
#(Opcional) Ejemplo: minimum([])  debería devolver False

def minimo(lista):
    valor_max = lista[0]
    for i in lista:
        if i > valor_max:
            valor_max = i
    return valor_max   

print(minimo([37,2,1,-9]))


