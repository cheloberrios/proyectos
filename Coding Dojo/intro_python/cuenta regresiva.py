#11
#Cuenta regresiva - 
# Crea una función que acepte un número como entrada.
#  Devuelve una lista nueva que cuenta de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento).
#Ejemplo: cuentaregresiva(5) debe devolver la lista: [5,4,3,2,1,0]
def reg(n):
    for i in range(n, 0, -1):
        print(i)

reg(5)

