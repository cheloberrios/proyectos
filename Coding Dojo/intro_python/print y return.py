#Crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#Ejemplo: : print_and_return([1,2]) debe imprimir 1 y devolver 2
def print_return(lista):
     print(lista[0])
     return lista[1]

lista = [3,4]
a = print_return(lista)
print(a)