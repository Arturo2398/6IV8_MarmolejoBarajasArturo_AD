import pandas as pd

##escribir un programa que le pregunte al usuario por las ventas de un rango de años y muestre en la pantalla una serie de datos de ventas indexadas 
##por los años antes y despues de aplicar un descuento 

inicio = int(input("Itroduce el año de ventas inicial: "))

fin = int(input("Introduce eñ año final de ventas"))

ventas = {}

for i in range(inicio,fin+1):
    ventas[i] = float(input("Introduce las ventas del año " + str(i) +':'))
    

ventas = pd.Series(ventas)

print('Ventas\n', ventas)
print('Ventas con decuento\n', ventas*0.9)