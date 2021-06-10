# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:33:20 2021

@author: Sofii
"""

class FormatoTabla():
        
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
    
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))
    
    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
 

class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        j = ""
        for h in headers:
            j += "<th>" + h + "</th>"
        print(f'<tr>{j}</tr>')
    
  
    def fila(self, data_fila):
        j = ""
        for h in data_fila:
            j += "<td>" + h + "</td>"
        print(f'<tr>{j}</tr>')

def crear_formateador(fmt):
    if fmt == "txt":
        forma = FormatoTablaTXT()
        
    elif fmt == "html":
        forma = FormatoTablaHTML()
        
    elif fmt == "csv":
        forma = FormatoTablaCSV()
        
    else:    
        raise RuntimeError(f'Unknown format {fmt}')
    return forma
