import re
from funciones_ocr import extraer_texto

texto = extraer_texto("contrato_1-1")



info_d_contr= []
def extraer_datos_contratista(lis):
    datos ={'Representante':'','Nombre':'','Cedula':''}
    patter_cedula = re.compile(r"identificado con cédula (\d)")
    


    


