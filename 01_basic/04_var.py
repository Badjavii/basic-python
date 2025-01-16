###
# 04 - Variable
# Las variables sirven para guardar datos en memoria.
# Python es un lenguaje de tipado dinámico y fuerte.
###

# Asignación de dato str a una variable
my_name = "badjavii"
print("Mi nombre es: ", my_name, end=". ")

# Asignación de dato int a una variable
age = 19
print("Actualmente tengo ", age, end=", pero dentro de unos meses tendre ")

# # Reasignación a la variable int
age = 20
print(age)

# Malas practicas de nombre de variables
# -- Las variables tienen que tener un nombre con caracteres pegados o, en su defecto, separados por '_'. --
# -- Las variables se deben nombrar en ingles y NO en español.--
MiNombreEs = ""
laedaddemihermano = 0

# f-string
print(f"Mi nombre es -{MiNombreEs}- y la edad de mi hermano es {laedaddemihermano}.")

# Reanotación del tipo de la variable
is_this_program_going_to_end: bool = True
is_this_program_going_to_end = 0
print(f"El contenido de la variable is_this_program_going_to_end es {is_this_program_going_to_end}") # Se le anota una etiqueta con el tipo, pero NO hará que el tipado sea estatico 