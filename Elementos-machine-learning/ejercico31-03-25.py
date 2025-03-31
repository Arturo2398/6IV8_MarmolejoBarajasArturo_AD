#Calculas las distancias entre todos los pares de puntos y determinaremos cuales estan mas alejados entre si
#y cuales estan mas cercanos utilizando la distancia euclidiana, de manhattan y de chebyshev.

import numpy as np
import pandas as pd
from scipy.spatial import distance

#definimos los puntos 
puntos = {
    'Punto A': [2, 3],
    'Punto B': [5, 4],
    'Punto C': [1, 1],
    'Punto D': [6, 7],
    'Punto E': [3, 5],
    'Punto F': [8, 2],
    'Punto G': [4, 6],
    'Punto H': [2, 1]
}

#Convertimos las coordenadas en un DataFrame
df = pd.DataFrame(puntos).T
df.columns = ['x', 'y']
print("Coordenadas de los puntos")
print(df)

def Caldistancias(puntos):
    distancias = pd.DataFrame(index=df.index, columns=df.index)
    #Calculo de las distancias
    for i in df.index:
        for k in df.index:
            if i!=k:
                distancias.loc[i, k] = distance.euclidean(df.loc[i], df.loc[k])
            else :
                distancias.loc[i, k] = 0
    return distancias
distancias = Caldistancias(puntos)
valor_max = distancias.values.max()

(punto1, punto2) = distancias.stack().idxmax()

print("tabala de distancias")
print(distancias)
print('Distacia maxima: ', valor_max)
print('Entre el punto: ', punto1, ' y el punto: ', punto2)

#De otra manera
max_Value = distancias.max().max()
#obtener la columna del valor maximo
max_Column = distancias.max().idxmax()
#obtener el indice del valor maximo
max_Index = distancias[max_Column].idxmax()
print('Distacia maxima: ', max_Value)