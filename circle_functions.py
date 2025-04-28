# -- coding: utf-8 -*-

from math import pi
import os

def circle_area(radius):
    '''
    Calcula el área de un círculo dado su radio.
    param radius: Radio del círculo
    return: Área del círculo
    '''
    area = pi * (radius ** 2)
    return area

def cylinder_volume(radius, height):
    '''
    Calcula el volumen de un cilindro dado su radio y altura.
    param radius: Radio de la base del cilindro
    param height: Altura del cilindro
    return: Volumen del cilindro
    '''
    base = circle_area(radius)
    volume = base * height
    return volume

def get_float_input(prompt):
    '''
    Solicita al usuario un número de punto flotante y maneja errores de entrada.
    param prompt: Mensaje para solicitar la entrada
    return: Número de punto flotante ingresado por el usuario
    '''
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
            os.system('cls' if os.name == 'nt' else 'clear')

radius = get_float_input("Ingrese el radio del círculo: ")
print("Área del círculo:", circle_area(radius))

radius_cylinder = get_float_input("Ingrese el radio del cilindro: ")
height_cylinder = get_float_input("Ingrese la altura del cilindro: ")
print("Volumen del cilindro:", cylinder_volume(radius_cylinder, height_cylinder))
