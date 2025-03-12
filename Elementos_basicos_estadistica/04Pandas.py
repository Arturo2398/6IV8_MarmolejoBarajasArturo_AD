import pandas as pd
import matplotlib.pyplot as plt



df = pd.read_csv('Elementos basicos de estadistica/housing.csv')

#mostrar las primeras 5 filas
print(df.head())

#mostar las ultiams 5 filas
print(df.tail())

#fila especifica s
print(df.iloc[7])

#mostrar la columna ocean_proximity
print(df["ocean_proximity"])

#obtener la media de la columna total_rooms
media = df['total_rooms'].mean()

print(f'La media de la columna total_rooms es: {media}')

#mediana
mediana = df['median_house_value'].median()

print(f'La mediana de la columna median_house_value es {mediana}')

#suma popular
salario = df['population'].sum()

print(f'el salario es {salario}')

#filtro
filtro= df[df['ocean_proximity'] == 'ISLAND']

print(filtro)

#grafico de dispercion
plt.scatter(df['ocean_proximity'] [:10], df['median_house_value'][:10])
#nombramos ls ejes 
plt.xlabel("Proximidad")
plt.ylabel("Precio")
plt.title("Grafico de dispercion de proximidad del oceano y precio")
plt.show()
