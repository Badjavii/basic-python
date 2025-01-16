###
# 03 - casting de types
# Transformar un tipo de un valor a otro
###

print("Conversión de tipos\n")
print("¿Que tipo de dato es 100?", type(int("100")))

print(2 + int(100))   # Suma algebraica
print("100" + str(2)) # Concatenación de cadenas de caracteres (string)

print(float("3.1416")) # Conversión de string a float
print(int(3.1426))     # Conversión de int a float (elimina los decimales)

print(bool(3))  # Todos los int diferentes a cero darán true
print(bool(0))  # El 0 es false
print(bool(-1))

print(bool(""))
print(bool(" "))
print(bool("False"))