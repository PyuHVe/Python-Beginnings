# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:26:50 2025

@author: je.oviedo
"""

import module as m

def ejecutar_perdida_de_peso_despues_de_un_mes()-> None:
    w = float(input("Digite el peso en kilógramos: "))
    p = float(input("Digite el porcentaje de grasa corporal: "))
    print("Su peso al cabo de un mes será:", round(m.peso_despues_de_un_mes(w, p), 2), "kilógramos")
    
def iniciar_aplicacion()-> None:
    print("Bienvenido a la calculadora de perdida de peso")
    ejecutar_perdida_de_peso_despues_de_un_mes()


iniciar_aplicacion()