# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:26:26 2025

@author: je.oviedo
"""

import cupify as c

def ejecutar_calcular_tarifa_total()-> None:
    dr = float(input("Digite la distancia recorrida en kilómetros: "))
    tt = float(input("Digite el tiempo transcurrido en minutos: "))
    ind = float(input("Digite el índice de demanda (Valor entre [-0.2,0.2]): "))
    print("La tarifa total es de:", c.calcular_tarifa_total(dr, tt, ind), "pesos")    
    
def iniciar_aplicacion()-> None:
    print("¡Bienvenido a la calculadora de la tarifa total!")
    ejecutar_calcular_tarifa_total()


iniciar_aplicacion()
