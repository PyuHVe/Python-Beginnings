# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:41:32 2025

@author: je.oviedo
"""

def calorias_a_perder(peso_actual: float, peso_final: float)-> float:
    kilos_perder = peso_actual - peso_final
    return kilos_perder * 7700

def semanas_para_adelgazar(peso_actual: float, peso_final: float, tiempo_deporte: float)-> float:
    calorias_perder = calorias_a_perder(peso_actual, peso_final)
    calorias_semana = 2800 + 10 * tiempo_deporte
    return calorias_perder / calorias_semana

