import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('Elementos_basicos_estadistica/housing.csv')

estadisticas = df["median_house_value"].agg(["mean", "median", "var", "std"]).to_frame()

estadisticas.loc["Moda"] = df["median_house_value"].mode().values[0]
estadisticas.loc["Rango"] = np.ptp(df["median_house_value"])

estadisticas.index = ["Media", "Mediana", "Varianza", "Desviación Estándar", "Moda", "Rango"]

estadisticas_df = estadisticas.reset_index()
estadisticas_df.columns = ["Estadística", "Valor"]

limites_clases = range(int(df["median_house_value"].min()), int(df["median_house_value"].max()) + 50000, 50000)
df["Intervalo"] = pd.cut(df["median_house_value"], bins=limites_clases, right=False)

tabla_frecuencias = df["Intervalo"].value_counts().reset_index()
tabla_frecuencias.columns = ["Intervalo de Valores", "Frecuencia"]
tabla_frecuencias = tabla_frecuencias.sort_values(by="Intervalo de Valores")

print("\n================ ESTADÍSTICAS DESCRIPTIVAS ================".center(80))
print(estadisticas_df.to_string(index=False))
print("\n================= TABLA DE FRECUENCIAS =================".center(80))
print(tabla_frecuencias.to_string(index=False))

df[["median_house_value", "total_bedrooms", "population"]].hist(bins=30, alpha=0.5, figsize=(10, 6))
plt.suptitle("Histograma Comparativo: Valor Medio de Vivienda vs Total de Dormitorios y Población")
plt.show()
