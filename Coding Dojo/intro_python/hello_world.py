# 1. TASK: print "Hola, mundo"
print("Hola, mundo ")
# 2. print "Hola Noelle!" con el nombre de una variable
name = "Marcelo"
print("Hola ", name )	# con una coma
print("Hola " + name )	# con un +
# 3. print "Hola 42!" con el número en una variable
name = 42
print("Hola ", name )	# con una coma
#print("Hola " + name )	# con un +	-- ¡esta nos debería arrojar un error!
# 4. print "Amo comer sushi y pizza." con las comidas en variables
fave_food1 = "papas fritas"
fave_food2 = "empanada"
print("amo comer {} y {}".format(fave_food1, fave_food2))
print(f"amo comer {fave_food1} y {fave_food2}" ) # with an f string
#otrosmetodos
name2 = "Marcelo"
print("me llamo %s y me gusta comer %s" % (name2, fave_food2))



