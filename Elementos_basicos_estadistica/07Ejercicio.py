import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Elementos_basicos_estadistica/proyecto1.csv')  
df2 = pd.read_csv('Elementos_basicos_estadistica/Catalogo_sucursal.csv')  


ventas_totales = df['ventas_tot'].sum()
socios_con_adeudo = df[df['adeudo_actual'] > 0].shape[0]
socios_sin_adeudo = df[df['adeudo_actual'] == 0].shape[0]
total_socios = socios_con_adeudo + socios_sin_adeudo
porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100
deuda_total = df['adeudo_actual'].sum()
utilidad = ventas_totales - deuda_total
porcentaje_utilidad = (utilidad / ventas_totales) * 100
 
print("\n=== RESULTADOS DEL ANÁLISIS ===")
print(f"\nVentas totales del comercio: ${ventas_totales:,.2f}")
print(f"\nAnálisis de Socios:")
print(f"- Con adeudo: {socios_con_adeudo} ({porcentaje_con_adeudo:.1f}%)")
print(f"- Sin adeudo: {socios_sin_adeudo} ({porcentaje_sin_adeudo:.1f}%)")
print(f"\nDeuda total de clientes: ${deuda_total:,.2f}")
print(f"Porcentaje de utilidad: {porcentaje_utilidad:.2f}%")
 
plt.figure(figsize=(12, 6))
df.groupby('B_mes')['ventas_tot'].sum().plot(kind='bar')
plt.title('Ventas Totales por Fecha')
plt.xlabel('Fecha')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45) 
plt.tight_layout()
plt.show()

df['pagos_tot'] = df['pagos_tot'].fillna('').astype(str).str.replace(',', '.').astype(float)


desviacion_estandar = df.groupby('B_mes')['pagos_tot'].std()
plt.figure(figsize=(10, 6))
plt.plot(desviacion_estandar, marker='o', color='red')
plt.title('Desviación Estándar de Pagos Realizados Respecto del Tiempo')
plt.xlabel('Mes')
plt.ylabel('Desviación Estándar')
plt.xticks(rotation=45)
plt.grid()
plt.show()

df['adeudo_actual'] = df['adeudo_actual'].fillna('').astype(str).str.replace(',', '.').astype(float)
deuda_total = df['adeudo_actual'].sum()


utilidad = ventas_totales - deuda_total
porcentaje_utilidad = (utilidad / ventas_totales) * 100

ventas_por_sucursal = df.groupby('id_sucursal')['ventas_tot'].sum().reset_index()
ventas_por_sucursal = ventas_por_sucursal.merge(df2, on='id_sucursal', how='left')
plt.figure(figsize=(8, 8))
plt.pie(ventas_por_sucursal['ventas_tot'], labels=ventas_por_sucursal['suc'], autopct='%1.1f%%', startangle=90)
plt.title('Ventas por Sucursal')
plt.show()

deudas_por_sucursal = df.groupby('id_sucursal')['adeudo_actual'].sum().reset_index()
deudas_por_sucursal = deudas_por_sucursal.merge(df2, on='id_sucursal', how='left')

utilidad_por_sucursal = ventas_por_sucursal['ventas_tot'] - deudas_por_sucursal['adeudo_actual']

plt.figure(figsize=(10, 6))
x = np.arange(len(deudas_por_sucursal['suc']))
plt.bar(x - 0.2, deudas_por_sucursal['adeudo_actual'], width=0.4, label='Deudas Totales', color='orange')
plt.bar(x + 0.2, utilidad_por_sucursal, width=0.4, label='Margen de Utilidad', color='green')
plt.xticks(x, deudas_por_sucursal['suc'], rotation=45)
plt.title('Deudas Totales y Margen de Utilidad por Sucursal')
plt.xlabel('Sucursal')
plt.ylabel('Monto')
plt.legend()
plt.tight_layout()
plt.show()