x = int(input("Ingrese una coordenada x"))
y = int(input("Ingrese una coordenada y"))
##Importamos libreria math para hacer funcionar el math.sqrt que seria raiz cuadrada.
import math
##Posicion cero o origen
x0 = 0 
y0 = 0
distancia = math.sqrt( (x-x0)**2 +(y-y0)**2 )

print (distancia)