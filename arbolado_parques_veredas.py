# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:10:10 2021

@author: Sofii
"""
import pandas as pd
import os
import seaborn as sns
#%%  Ejercicio 8.7
#Abro el archivo para veredas ubicado en el directorio especifico
directorio = '../Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df_veredas = pd.read_csv(fname)

#Armo un dataframe con las columnas seleccionadas
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df_veredas[cols_sel]

#Cuento la cantidad de ejemplares
cant_ejemplares = df_veredas['nombre_cientifico'].value_counts()

#Imprimo los 10 mas abundantes
#  print(f'10 especies mas abundantes:\n {cant_ejemplares.iloc[0:10]}')

#selecciono tres especies
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]

#%%  Ejercicio 8.8
#Hago un boxplot con las alturas de los arboles
#  df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

#Hago un gráfico con 4 gráficos adentro, una fila y columna por cada variable 
#numérica, en la daigonal va a haber kdeplots y  fuera scatterplots combinando 
#todos los pares de variables
#  sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')

#El ancho de la acera no tiene lugar en el gráfico porque es una varible no 
#numérica o porque tiene valores faltantes

#%%  Ejercicio 8.9

#Abro el archivo para árboles en  parques ya que el de veredas se abrio en el ejercicio 8.7
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df_parques = pd.read_csv(fname)

#Elijo las especie que quiero para hacer el boxplot con ambos ambientes
especie_vereda = 'Tipuana tipu'
especie_parque = 'Tipuana Tipu'

def box_plot(especie_vereda, especie_parque):
    #Creo un data set para cada tipo de espacio que incluya solo las tipas y hago una copia
    df_tipas_parques = df_parques[df_parques['nombre_cie'] == especie_parque ].copy()
    df_tipas_veredas = df_veredas[df_veredas['nombre_cientifico'] == especie_vereda].copy()
    
    #Elijo solo las columnas que voy a utilizar de cada dataset con tipas
    cols_par = ['altura_tot', 'diametro']
    cols_ver = ['altura_arbol', 'diametro_altura_pecho']
    df_tipas_parques = df_tipas_parques[cols_par]
    df_tipas_veredas = df_tipas_veredas[cols_ver]
    
    #Renombro comlumnas para que sean iguales en ambos data frame
    df_tipas_veredas = df_tipas_veredas.rename(columns={'altura_arbol': 'altura_tot', 'diametro_altura_pecho': 'diametro'})
    
    #Agrego a cada data frame una columna que indique su procedencia
    df_tipas_parques = df_tipas_parques.assign(Ambiente = "Parques")
    df_tipas_veredas = df_tipas_veredas.assign(Ambiente = "Veredas")
    
    #Junto ambos df en uno
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    
    #Hago un boxplot del diametro y otro de la altura por ambiente
    return df_tipas.boxplot('diametro', by = 'Ambiente'), df_tipas.boxplot('altura_tot', by = 'Ambiente')

box_plot(especie_vereda, especie_parque)

