# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:30:54 2021

@author: Sofii
"""
import csv

def parse_csv(nombre_archivo, select = None, types=False, has_headers=True, silence_errors=False):
    '''
    Parsea cualquier objeto o iterable que se comporte como un archivo en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, 
    que debe ser una lista de nombres de las columnas a considerar.
    '''
    #with open(nombre_archivo) as f:
    f = nombre_archivo
    filas = csv.reader(f)
    registros = []
    # Lee los encabezados del archivo
    
    if has_headers:
        encabezados = next(filas)
        
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
            
        else:
            indices = []
           
        for n_fila, fila in enumerate(filas, start=1):
            
           
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila) ]
                except ValueError as e: 
                    if not silence_errors:
                        print(f'Fila {n_fila}: No pude convertir {fila} \nFila {n_fila}: Motivo: {e}')
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
                
    else:
        if select and not silence_errors:
            raise RuntimeError("Para seleccionar, necesito encabezados.")
        else: 
            for n_fila, fila in enumerate(filas, start=1):
                if not fila:    # Saltear filas vacías
                       continue
                if types:
                    try:
                        fila = [func(val) for func, val in zip(types, fila) ]
                    except ValueError as e: 
                        if not silence_errors:
                            print(f'Fila {n_fila}: No pude convertir {fila} \nFila {n_fila}: Motivo: {e}')
                registros.append(tuple(fila))
    return registros

#camion = parse_csv('../Data/missing.csv', types = [str, int, float])
#camion = parse_csv('../Data/missing.csv', types = [str,int,float], silence_errors = True)
#camion = parse_csv('../Data/camion.csv', types=[str, int, float])
#precios = parse_csv('../Data/precios.csv', types=[str,float], has_headers=False)
#parse_csv('../Data/precios.csv', select = ['nombre','precio'], has_headers = False)

