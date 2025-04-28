# -- coding: utf-8 -*-

import os

def get_float_input(prompt, allow_empty=False, default=None):
    '''
    Solicita al usuario un número de punto flotante y maneja errores de entrada.
    param prompt: Mensaje para solicitar la entrada
    param allow_empty: Permite aceptar vacío (usado para valores opcionales como el IVA)
    param default: Valor por defecto si el usuario no ingresa nada
    return: Número de punto flotante ingresado por el usuario o valor por defecto
    '''
    while True:
        user_input = input(prompt)
        if allow_empty and user_input == "":
            return default
        try:
            return float(user_input)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
            os.system('cls' if os.name == 'nt' else 'clear')

def invoice_total(amount, vat=12):
    '''
    Calcula el total de la factura aplicando el porcentaje de IVA.
    param amount: Monto sin IVA
    param vat: Porcentaje de IVA (por defecto 12%)
    return: Total de la factura con IVA
    '''
    total = amount + (amount * vat / 100)
    return total

# Uso interactivo
amount = get_float_input("Ingrese el valor de la factura sin IVA: ")
vat = get_float_input(
        "Ingrese el porcentaje de IVA (presione Enter para usar 12% por defecto): ", 
        allow_empty=True, 
        default=12)

total = invoice_total(amount, vat)
print(f"Total de la factura con IVA {vat}%: {total}")
