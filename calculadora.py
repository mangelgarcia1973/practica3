#Calculadora con la ayuda de....
def sumar(a, b):
    return a + b

def calculadora():
    seguir = True
    while seguir:
        print("Calculadora simple en Python")
        print("Operaciones disponibles: +, -, *, /")

        a = float(input("Introduce el primer número para sumar: "))
        operacion = input("Introduce la operación (+, -, *, /): o S para salir")
        b = float(input("Introduce el segundo número para sumar: "))    


        if operacion == "+":
            resultado = sumar(a, b)
            

        seguir = operacion != "S"


# Ejecutar la calculadora
calculadora()