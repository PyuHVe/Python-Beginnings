# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:25:47 2025

@author: je.oviedo
"""

import cupify as c 

def ejecutar_calcular_tarifa_base()-> None:
    dr = float(input("Digite la distancia recorrida en kilómetros: "))
    tt = float(input("Digite el tiempo transcurrido en minutos: "))
    print("La tarifa base es de:", c.calcular_tarifa_base(dr, tt), "pesos") 

def iniciar_aplicacion()-> None:
    print("¡Bienvenido a la calculadora de la tarifa base!")
    ejecutar_calcular_tarifa_base()
 

iniciar_aplicacion()