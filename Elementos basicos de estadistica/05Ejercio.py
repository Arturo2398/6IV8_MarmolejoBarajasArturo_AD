import pandas as pd
import matplotlib.pyplot as plt

#moda media rango varianza y desviacion con la tabla de frecuenias del housing

def housing(fichero):
    df = pd.read_csv(fichero, sep=';',decimal=',',thousands='.', index_col=0)
    return pd.DataFrame([df.mean(),df.median, df.mode(),df.max()-df.min(),df.var(),df.std()], index = ['media','mediana','moda','rango','varianza','Desviacion Estandar'])



print(housing('Elementos basicos de estadistica/housing.csv'))

