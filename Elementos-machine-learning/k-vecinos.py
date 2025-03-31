import numpy as np
import pandas as pd
from scipy.spatial import distance

#definimos las coordenadas de las tiendas
tiendas = {
    'Tienda A': [1, 1],
    'Tienda B': [1, 5],
    'Tienda C': [7, 1],
    'Tienda D': [3, 3],
    'Tienda E': [4, 8]
}

#Convertimos las coordenadas en un DataFrame
df = pd.DataFrame(tiendas).T
df.columns = ['x', 'y']
print("Coordenadas de las tiendas")
print(df)

#Inicializamos un dataframe para guardar las distancias
distancias_eu = pd.DataFrame(index=df.index, columns=df.index)
distancias_mh = pd.DataFrame(index=df.index, columns=df.index)
distancias_ch = pd.DataFrame(index=df.index, columns=df.index)

#Calclas las distancias

for i in df.index:
    for j in df.index:
        #distancia euclidiana
        distancias_eu.loc[i, j] = distance.euclidean(df.loc[i], df.loc[j])
        #distancia de manhattan
        distancias_mh.loc[i, j] = distance.cityblock(df.loc[i], df.loc[j])
        #distancia de chebyshev
        distancias_ch.loc[i, j] = distance.chebyshev(df.loc[i], df.loc[j])
        
#Mostramos los resultados
print("\nDistancia euclidiana")
print(distancias_eu)
print("\nDistancia de Manhattan")
print(distancias_mh)
print("\nDistancia de Chebyshev")
print(distancias_ch)