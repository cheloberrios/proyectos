students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

print(f'first_name - {students[0]["first_name"]}, last_name - {students[0]["last_name"]}')

def iterateDictionary(lista):
    x=0
    for i in lista:
        print(f'first_name - {students[x]["first_name"]}, last_name - {students[x]["last_name"]}')
        x = x+1
        

iterateDictionary(students) 
# debería generar: (está bien si cada par llave-valor termina en 2 líneas separadas;
# ¡bonificación para que aparezcan exactamente como se muestra a continuación!)
#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel
