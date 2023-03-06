students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(key, lista):
    x=0
    for i in lista:
        print(lista[x][key])
        x = x+1
        

iterateDictionary(key='first_name', lista = students) 
# debería generar: (está bien si cada par llave-valor termina en 2 líneas separadas;
# ¡bonificación para que aparezcan exactamente como se muestra a continuación!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel
