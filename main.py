from __init__ import *


texto ="El señor Diego Andres Cardona identificado con cédula 1234 en representación de Casalimpia"

texto = texto.split()
# extraemos datos del contratante
datos = extraer_datos_contratante(texto,'Cédula','Representación')
