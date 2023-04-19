def pauta_alimenticia_barf(peso, tamaño, actividad, castrado, raza, edad):
    # calcular la cantidad de comida necesaria, según la fórmula de Barf y los datos de entrada
    cantidad_total = peso * (2 if actividad == 'baja' else 3) / 100
    cantidad_carne = cantidad_total * 0.7
    cantidad_huesos = cantidad_total * 0.1
    cantidad_frutas_verduras = cantidad_total * 0.1
    cantidad_lacteos = cantidad_total * 0.05
    cantidad_aceites_grasas = cantidad_total * 0.05
    
    # devolver la pauta alimenticia de Barf, en gramos
    return {
        "carne": cantidad_carne,
        "huesos": cantidad_huesos,
        "frutas_verduras": cantidad_frutas_verduras,
        "lacteos": cantidad_lacteos,
        "aceites_grasas": cantidad_aceites_grasas
    }

# Solicitar los datos de entrada del usuario
peso = float(input("Ingrese el peso de su perro en kg: "))
tamaño = input("Ingrese el tamaño de su perro (pequeño, mediano o grande): ")
actividad = input("Ingrese la actividad de su perro (baja, media o alta): ")
castrado = input("¿Está su perro castrado? (sí o no): ")
raza = input("Ingrese la raza de su perro: ")22
edad = float(input("Ingrese la edad de su perro en años: "))

# Calcular la pauta alimenticia de Barf
pauta = pauta_alimenticia_barf(peso, tamaño, actividad, castrado, raza, edad)

# Imprimir la proporción de cada tipo de alimento
print(f"Proporción de alimento para una dieta Barf de {peso} kg de un perro {tamaño} y {actividad} de actividad:")
print(f"Carne: {round(pauta['carne'])} gramos")
print(f"Huesos: {round(pauta['huesos'])} gramos")
print(f"Frutas y verduras: {round(pauta['frutas_verduras'])} gramos")
print(f"Lácteos: {round(pauta['lacteos'])} gramos")
print(f"Aceites y grasas: {round(pauta['aceites_grasas'])} gramos")
