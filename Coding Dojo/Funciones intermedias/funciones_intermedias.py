import random
def randInt(min=0 , max=100):
    num = random.random() * max
    if min > max:
        print("minimo es mayor que maximo")
    if max < 0:
        print("maximo es menor que 0")
    return num
#print(randInt() 	        	# debe imprimir un número entero aleatorio entre 0 y 100
#print(randInt(max=50)) 	        # debe imprimir un número entero aleatorio entre 0 y 50
#print(randInt(min=50)) 	            # debe imprimir un número entero aleatorio entre 50 y 100
#print(randInt(min=50, max=500))    # debe imprimir un número entero aleatorio entre 50 y 500
#print(randInt(min=0, max=-2))         # caso de borde
