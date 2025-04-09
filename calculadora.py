#Calculadora con la ayuda de....



def calculadora():
    seguir = True
    while seguir:
        print("Calculadora simple en Python")
        print("Operaciones disponibles: +, -, *, /")

        a = float(input("Introduce el primer número: "))
        operacion = input("Introduce la operación (+, -, *, /): o S para salir")
        b = float(input("Introduce el segundo número: "))    
        seguir = operacion != "S"

# Ejecutar la calculadora
calculadora()