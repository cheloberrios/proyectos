#Lista inversa (opcional) -
#Crea una función que tome una lista 
#y devuelva esa lista con los valores invertidos.  
#Haz esto sin crear una segunda lista. 
#(Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
#Ejemplo: reverse_list([37,2,1,-9]) debería devolver [-9,1,2,37]

def invertida(lista):
    for i in range(len(lista)//2):
        lista[i], lista[len(lista)-i-1] = lista[len(lista)-i-1], lista[i]
        print(lista)
    print(lista)
invertida([37,2,1,-9])