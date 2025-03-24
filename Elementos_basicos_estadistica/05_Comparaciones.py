import numpy as np
import matplotlib.pyplot as plt

#creamos una semilla aleatoria para reproductividad

np.random.seed(0)

#Buscamos los parametros para una distribucion
#media
media = 0

#desviacion estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

# Numero de muestras ara el analiisis

n_muestra = 1000

#Generamos los datos d las distribuciones normales

data1 = np.random.normal(media, sigma1, n_muestra)
data2 = np.random.normal(media, sigma2, n_muestra)
data3 = np.random.normal(media, sigma3, n_muestra)

#le damos forma a la grafica

plt.figure(figsize=(10,6))

#Cargamos las freciencias a partir de un histograma

plt.hist(data1, bins=50, density=True, color='blue', label='Desciacion estandar 1', alpha=0.5)
plt.hist(data2, bins=50, density=True, color='red', label='Desviacion estandar 2', alpha=0.5)
plt.hist(data3, bins=50, density=True, color='green', label='Desviacon estandar 3', alpha=0.5)

plt.title('Comparacion de distribuciones normales con una semilla en random')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')
plt.legend()
plt.grid()

plt.show()