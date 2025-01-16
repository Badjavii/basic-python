###
# 05 - Entrada de datos (input())
# Las variables sirven para guardar datos en memoria.
# La función input() permite obtener datos del usuario a través de la consola.
###

name = input("Bienvenido, ingrese su nombre: ")
print(f"Hola {name}, encantado en conocerte.")

age = int(input("Ingresa tu edad: "))
print(f"Tienes {age} años.")


country, city = input("Ingresa tu pais y ciudad de nacimiento en la misma linea: ").split()
print(f"Vives en {city}, {country}.")