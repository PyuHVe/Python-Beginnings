# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:08:42 2025

@author: je.oviedo
"""

def gramos_por_semana(peso: float, porcentaje_grasa: float)-> float:
    kilos_grasa = peso * porcentaje_grasa/100
    klc_dia = 70
    return (klc_dia * kilos_grasa / 9) * 7

def peso_despues_de_un_mes(peso: float, porcentaje_grasa: float)-> float:
    semana1 = gramos_por_semana(peso, porcentaje_grasa) / 1000
    peso1 = peso - semana1
    semana2 = gramos_por_semana(peso1, porcentaje_grasa) / 1000
    peso2 = peso1 - semana2
    semana3 = gramos_por_semana(peso2, porcentaje_grasa) / 1000
    peso3 = peso2 - semana3
    semana4 = gramos_por_semana(peso3, porcentaje_grasa) / 1000
    peso4 = peso3 - semana4
    return peso4