# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:26:08 2025

@author: je.oviedo
"""

import cupify as c

def ejecutar_calcular_tarifa_dinamica()-> None:
    dr = float(input("Digite la distancia recorrida en kilómetros: "))
    tt = float(input("Digite el tiempo transcurrido en minutos: "))
    ind = float(input("Digite el índice de demanda (Valor entre [-0.2,0.2]): "))
    print("La tarifa dinamica es de:", c.calcular_tarifa_dinamica(dr, tt, ind), "pesos")

def iniciar_aplicacion()-> None:
    print("¡Bienvenvenido a la calculadora de la tarifa dinamica!")
    ejecutar_calcular_tarifa_dinamica()
    
    
iniciar_aplicacion()
