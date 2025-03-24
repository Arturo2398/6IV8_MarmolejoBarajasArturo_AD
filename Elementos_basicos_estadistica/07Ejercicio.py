import pandas as pd
import matplotlib.pyplot as plt

# Espacio para cargar los archivos con los datos
# df_ventas = pd.read_csv('ventas.csv')
# df_socios = pd.read_csv('socios.csv')

# Calcular ventas totales
# ventas_totales = df_ventas['monto'].sum()

# Calcular número de socios con y sin adeudo
# socios_con_adeudo = df_socios[df_socios['adeudo'] > 0].shape[0]
# socios_sin_adeudo = df_socios[df_socios['adeudo'] == 0].shape[0]

# Calcular deuda total
# deuda_total = df_socios['adeudo'].sum()

# Calcular porcentaje de utilidad
# utilidad = ventas_totales - deuda_total
# porcentaje_utilidad = (utilidad / ventas_totales) * 100

# Graficar ventas totales
# plt.figure(figsize=(10, 6))
# df_ventas.groupby('fecha')['monto'].sum().plot(kind='bar')
# plt.title('Ventas Totales por Fecha')
# plt.xlabel('Fecha')
# plt.ylabel('Monto')
# plt.show()

# Graficar número de socios con y sin adeudo
# plt.figure(figsize=(10, 6))
# plt.bar(['Con Adeudo', 'Sin Adeudo'], [socios_con_adeudo, socios_sin_adeudo], color=['red', 'green'])
# plt.title('Número de Socios con y sin Adeudo')
# plt.xlabel('Estado de Adeudo')
# plt.ylabel('Número de Socios')
# plt.show()

# Imprimir resultados
# print(f"Ventas Totales: {ventas_totales}")
# print(f"Número de Socios con Adeudo: {socios_con_adeudo}")
# print(f"Número de Socios sin Adeudo: {socios_sin_adeudo}")
# print(f"Deuda Total: {deuda_total}")
# print(f"Porcentaje de Utilidad: {porcentaje_utilidad:.2f}%")