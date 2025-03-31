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

def calcular_distancia(df, tipo='euclidean'):
    distancias = pd.DataFrame(index=df.index, columns=df.index)
    for i in df.index:
        for k in df.index:
            if i!=k:
                if tipo == 'euclidean':
                    distancias.loc[i, k] = distance.euclidean(df.loc[i], df.loc[k])
                elif tipo == 'manhattan':
                    distancias.loc[i, k] = distance.cityblock(df.loc[i], df.loc[k])
                elif tipo == 'chebyshev':
                    distancias.loc[i, k] = distance.chebyshev(df.loc[i], df.loc[k])
            else:
                distancias.loc[i, k] = 0
    return distancias

# Calculamos las tres distancias
print("\n=== DISTANCIA EUCLIDIANA ===")
distancias_euclidean = calcular_distancia(df, 'euclidean')
valor_max = distancias_euclidean.values.max()
punto1, punto2 = distancias_euclidean.stack().idxmax()
print("\nMatriz de distancias euclidianas:")
print(distancias_euclidean)
print('Distancia euclidiana máxima:', valor_max)
print('Entre el punto:', punto1, 'y el punto:', punto2)

print("\n=== DISTANCIA MANHATTAN ===")
distancias_manhattan = calcular_distancia(df, 'manhattan')
valor_max = distancias_manhattan.values.max()
punto1, punto2 = distancias_manhattan.stack().idxmax()
print("\nMatriz de distancias manhattan:")
print(distancias_manhattan)