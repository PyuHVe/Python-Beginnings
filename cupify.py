# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:19:00 2025

@author: je.oviedo
"""

def calcular_tarifa_distancia(distancia_recorrida: float)-> float:
    """ Esta función calcula la tarifa basada en la distancia recorrida
    Parámetros:
        distancia_recorrida (float): Distancia recorrida en kilómetros (valor mayor o igual a 0.0)
    Retorno:
        float: Tarifa por distancia, redondeada a dos decimales
    """
    costo_kilometro = 500
    return round(costo_kilometro * distancia_recorrida, 2)

def calcular_tarifa_tiempo(tiempo_transcurrido: float)-> float:
    """ Esta función calcula la tarifa basada en el tiempo transcurrido
    Parámetros:
        tiempo_transcurrido (float): Tiempo transcurrido en minutos (valor mayor o igual a 0.0)
    Retorno:
        float: Tarifa por tiempo, redondeada a dos decimales
    """
    costo_minuto = 250
    return round(costo_minuto * tiempo_transcurrido, 2)

def calcular_tarifa_base(distancia_recorrida: float, tiempo_transcurrido: float)-> float: 
    """ Esta función calcula la tarifa base considerando las tarifas por distancia 
        y tiempo e incluyendo el cobro base.
    Parámetros:
        distancia_recorrida (float): Distancia recorrida en kilómetros (valor mayor o igual a 0.0)
        tiempo_transcurrido (float): Tiempo transcurrido en minutos (valor mayor o igual a 0.0)
    Retorno:
        float: Tarifa base, redondeada a dos decimales
    """
    cobro_base = 2700
    tarifa_base = cobro_base + calcular_tarifa_distancia(distancia_recorrida) + calcular_tarifa_tiempo(tiempo_transcurrido)
    return round(tarifa_base, 2)

def calcular_tarifa_dinamica(distancia_recorrida: float, tiempo_transcurrido: float, indice_demanda: float)-> float:
    """ Esta función calcula la tarifa dinámica ajustada según el índice de demanda
    Parámetros:
        distancia_recorrida (float): Distancia recorrida en kilómetros (valor mayor o igual a 0.0)
        tiempo_transcurrido (float): Tiempo transcurrido en minutos (valor mayor o igual a 0.0)
        indice_demanda (float): Índice de demanda (valor entre -0.2 y 0.2)
    Retorno:
        float: Tarifa dinámica, redondeada a dos decimales
    """
    tarifa_base = calcular_tarifa_base(distancia_recorrida, tiempo_transcurrido)
    return round(tarifa_base * (1 + (indice_demanda / abs(1 + indice_demanda))), 2)

def calcular_tarifa_total(distancia_recorrida: float, tiempo_transcurrido: float, indice_demanda: float)-> float:
    """ Esta función calcula la tarifa total incluyendo el IVA
    Parámetros:
        distancia_recorrida (float): Distancia recorrida en kilómetros (valor mayor o igual a 0.0)
        tiempo_transcurrido (float): Tiempo transcurrido en minutos (valor mayor o igual a 0.0)
        indice_demanda (float): Índice de demanda (valor entre -0.2 y 0.2)
    Retorno:
        float: Tarifa total, redondeada a dos decimales
    """
    IVA = 0.19
    tarifa_dinamica = calcular_tarifa_dinamica(distancia_recorrida, tiempo_transcurrido, indice_demanda)
    return round(tarifa_dinamica * (1 + IVA), 2)

def calcular_ganancia_conductor(distancia_recorrida: float, tiempo_transcurrido: float, indice_demanda: float, calificacion_conductor: int)-> float:
    """ Esta función calcula la ganancia del conductor como un porcentaje de la tarifa dinámica (antes de impuestos), incluyendo una 
        bonificación adicional basada en la calificación del conductor
    Parámetros: 
        distancia_recorrida (float): Distancia recorrida en kilómetros (valor mayor o igual a 0.0)
        tiempo_transcurrido (float): Tiempo transcurrido en minutos (valor mayor o igual a 0.0)
        indice_demanda (float): Índice de demanda (valor entre -0.2 y 0.2)
        calificacion_conductor (int): Calificación del conductor (valor entre 0 y 5)
    Retorno:
        float: Ganancia del conductor, redondeada a dos decimales
    """
    porcentaje_conductor = 0.7
    tarifa_dinamica = calcular_tarifa_dinamica(distancia_recorrida, tiempo_transcurrido, indice_demanda)
    factor_bonificacion = 100
    return round(tarifa_dinamica * porcentaje_conductor + (factor_bonificacion * calificacion_conductor), 2)


