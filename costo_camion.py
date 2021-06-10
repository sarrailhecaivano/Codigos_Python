
from informe import leer_camion


def costo_camion(nombre_archivo):
    dic_cam= leer_camion('../Data/missing.csv')
    costo_total=0

    for line in dic_cam:
       
        try:

            ncajones = int(line.cajones)
            precio = float(line.precio)
            costo_total += ncajones * precio
        except:
            print (f'No pude interpretar: {line}, ¡Cuidado! hay valores vacios')	
					
    print('Costo total:', costo_total)


    return costo_total


costo = costo_camion('../Data/camion.csv')
costo2= costo_camion("../Data/fecha_camion.csv")


