import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar datos
df = pd.read_csv('Elementos_basicos_estadistica/housing.csv')

# Calcular estadísticas descriptivas con Pandas
stats_pandas = df["median_house_value"].agg(["mean", "median", "var", "std"]).to_frame()

# Agregar moda y rango manualmente
stats_pandas.loc["Moda"] = df["median_house_value"].mode().values[0]
stats_pandas.loc["Rango"] = np.ptp(df["median_house_value"])

# Renombrar índices para mayor claridad
stats_pandas.index = ["Media", "Mediana", "Varianza", "Desviación Estándar", "Moda", "Rango"]

# Convertir a DataFrame para mostrar
stats_pandas_df = stats_pandas.reset_index()
stats_pandas_df.columns = ["Estadística", "Valor"]

# Crear tabla de frecuencias con intervalos de 50,000 en 50,000
bin_edges = range(int(df["median_house_value"].min()), int(df["median_house_value"].max()) + 50000, 50000)
df["intervalo"] = pd.cut(df["median_house_value"], bins=bin_edges, right=False)
freq_table_pandas = df["intervalo"].value_counts().reset_index()
freq_table_pandas.columns = ["Intervalo de Valores", "Frecuencia"]
freq_table_pandas = freq_table_pandas.sort_values(by="Intervalo de Valores")

# Mostrar estadísticas descriptivas en formato tabla
print("\n================ ESTADÍSTICAS DESCRIPTIVAS ================".center(80))
print(stats_pandas_df.to_string(index=False))
print("\n================= TABLA DE FRECUENCIAS =================".center(80))
print(freq_table_pandas.to_string(index=False))

# Crear histogramas
df[["median_house_value", "total_bedrooms", "population"]].hist(bins=30, alpha=0.5, figsize=(10, 6))
plt.suptitle("Histograma Comparativo: Median House Value vs Total Bedrooms y Population")
plt.show()