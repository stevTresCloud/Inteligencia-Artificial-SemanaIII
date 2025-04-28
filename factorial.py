# -- coding: utf-8 -*-

import os

def get_positive_integer_input(prompt):
    '''
    Solicita al usuario un número entero positivo y maneja errores de entrada.
    param prompt: Mensaje para solicitar la entrada
    return: Número entero positivo ingresado por el usuario
    '''
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Por favor, ingrese un número entero positivo.")
            else:
                return value
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero válido.")
            os.system('cls' if os.name == 'nt' else 'clear')

def factorial(number):
    '''
    Calcula el factorial de un número entero positivo.
    param number: Número entero positivo
    return: Factorial del número
    '''
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

# Uso interactivo
number = get_positive_integer_input("Ingrese un número entero positivo para calcular su factorial: ")
print(f"El factorial de {number} es: {factorial(number)}")
