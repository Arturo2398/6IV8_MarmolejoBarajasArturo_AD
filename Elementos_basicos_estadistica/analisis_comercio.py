import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar archivos
df_catalogo = pd.read_csv('Elementos_basicos_estadistica/Catalogo_sucursal.csv')
df_proyecto = pd.read_csv('Elementos_basicos_estadistica/proyecto1.csv')

# Cálculos básicos
ventas_totales = df_proyecto['ventas_tot'].sum()
socios_con_adeudo = df_proyecto[df_proyecto['adeudo_actual'] > 0].shape[0]
socios_sin_adeudo = df_proyecto[df_proyecto['adeudo_actual'] == 0].shape[0]
total_socios = socios_con_adeudo + socios_sin_adeudo
porcentaje_con_adeudo = (socios_con_adeudo / total_socios) * 100
porcentaje_sin_adeudo = (socios_sin_adeudo / total_socios) * 100
deuda_total = df_proyecto['adeudo_actual'].sum()
utilidad = ventas_totales - deuda_total
porcentaje_utilidad = (utilidad / ventas_totales) * 100

# Imprimir resultados
print("\n=== RESULTADOS DEL ANÁLISIS ===")
print(f"\nVentas totales del comercio: ${ventas_totales:,.2f}")
print(f"\nAnálisis de Socios:")
print(f"- Con adeudo: {socios_con_adeudo} ({porcentaje_con_adeudo:.1f}%)")
print(f"- Sin adeudo: {socios_sin_adeudo} ({porcentaje_sin_adeudo:.1f}%)")
print(f"\nDeuda total de clientes: ${deuda_total:,.2f}")
print(f"Porcentaje de utilidad: {porcentaje_utilidad:.2f}%")

# Gráfica 1: Ventas totales por tiempo
plt.figure(figsize=(12, 6))
df_proyecto.groupby('B_mes')['ventas_tot'].sum().plot(kind='bar')
plt.title('Ventas Totales por Fecha')
plt.xlabel('Fecha')
plt.ylabel('Ventas Totales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfica 2: Desviación estándar de pagos
pagos_tiempo = df_proyecto.groupby('fec_ini_cdto')['pago_tot'].agg(['mean', 'std'])
plt.figure(figsize=(12, 6))
plt.errorbar(range(len(pagos_tiempo)), 
             pagos_tiempo['mean'], 
             yerr=pagos_tiempo['std'], 
             fmt='o-',
             capsize=5)
plt.title('Desviación Estándar de Pagos por Fecha')
plt.xlabel('Período')
plt.ylabel('Monto de Pago')
plt.tight_layout()
plt.show()

# Gráfica 3: Ventas por sucursal (circular)
ventas_por_sucursal = df_proyecto.groupby('id_sucursal')['ventas_tot'].sum()
plt.figure(figsize=(10, 8))
plt.pie(ventas_por_sucursal, labels=ventas_por_sucursal.index, autopct='%1.1f%%')
plt.title('Distribución de Ventas por Sucursal')
plt.axis('equal')
plt.show()

# Gráfica 4: Deudas vs Utilidad por sucursal
plt.figure(figsize=(12, 6))
deudas_sucursal = df_proyecto.groupby('suc')['adeudo_actual'].sum()
utilidad_sucursal = df_proyecto.groupby('suc').apply(
    lambda x: x['ventas_tot'].sum() - x['adeudo_actual'].sum())

x = np.arange(len(deudas_sucursal))
width = 0.35

plt.bar(x - width/2, deudas_sucursal, width, label='Deudas', color='red', alpha=0.6)
plt.bar(x + width/2, utilidad_sucursal, width, label='Utilidad', color='green', alpha=0.6)
plt.xlabel('Sucursal')
plt.ylabel('Monto')
plt.title('Deudas vs Utilidad por Sucursal')
plt.xticks(x, deudas_sucursal.index)
plt.legend()
plt.tight_layout()
plt.show()

