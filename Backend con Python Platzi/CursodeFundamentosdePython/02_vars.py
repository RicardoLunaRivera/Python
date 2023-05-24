print("Hola Vars")

# tipos de Variables

# String -> Cadena de Texto
my_name = "Ricardo"
print(my_name)
print(type(my_name))

# Int -> Entero
my_age = 28
print(my_age)
print(type(my_age))

# Double -> Entero con punto flotante /fracción
my_budget = 100.50
print(my_budget)
print(type(my_budget))

# Bool -> Boleano: solo 2 opciones True or False
is_married = False
print(is_married)
print(type(is_married))

print(f"Hola {my_name}, tienes {my_age}.\n"
      f"Tu valance actua en el banco es {my_budget}.")

#Input -> funcion para solicitar al usuario que ingrese algun dato
#NOTA -> Todo valor ingresado por "input" es del tipo string

your_name = input("Ingresa tu nombre: ")
print(your_name)
print(type(your_name))

#El tipo de dato de un valor ingesado por input puede ser modificado
your_age = input("Ingresa tu edad: ")
print(your_age)
print(type(your_age)) #string
your_age = int(your_age) #casteo a Int
print(your_age)
print(type(your_age)) #int

#optimización de código -> your_age = int(intput("Ingresa tu edad: "))