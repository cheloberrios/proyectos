#Lista inversa (opcional) -
#Crea una función que tome una lista 
#y devuelva esa lista con los valores invertidos.  
#Haz esto sin crear una segunda lista. 
#(Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list([37,2,1,-9]) debería devolver [-9,1,2,37]

def invertida(lista):
    for i in lista:
        numero1 = lista[0]
        lista.append(numero1)
        del lista[0]
        print(lista)
    print(lista)
invertida([37,2,1,-9])