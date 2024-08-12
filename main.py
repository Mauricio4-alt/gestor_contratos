from __init__ import *


texto ="El senor Diego Andres Cardona identificado con cédula 1234 en representación de Casalimpia"

texto = texto.split()
# extraemos datos del contratante
contratante ={'nombre':None,'representante':None,'cedula':None}
datos_contratante = extraer_datos(texto,contratante)






print(datos_contratante)
