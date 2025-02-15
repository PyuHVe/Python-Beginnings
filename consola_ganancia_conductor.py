# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 17:26:39 2025

@author: je.oviedo
"""

import cupify as c

def ejecutar_calcular_ganancia_conductor()-> None:
    dr = float(input("Digite la distancia recorrida en kilómetros: "))
    tt = float(input("Digite el tiempo transcurrido en minutos: "))
    ind = float(input("Digite el índice de demanda (Valor entre [-0.2,0.2]): "))
    cd = float(input("Digite la calificación del conductor (Valor entre [0,5] solo enteros): "))
    print("La ganancia del conductor es de:", c.calcular_ganancia_conductor(dr, tt, ind, cd), "pesos")

def iniciar_aplicacion()-> None:
    print("¡Bienvenido a la calculadora de la ganancia del conductor!")
    ejecutar_calcular_ganancia_conductor()
    
    
iniciar_aplicacion()