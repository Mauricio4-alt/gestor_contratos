import re
from funciones_ocr import extraer_texto

texto = extraer_texto("contrato_1-1")

pattern= re.compile('(el contratante?)',re.IGNORECASE)
match = pattern.search(texto)
print(match)
info_d_contr= []
def extraer_datos_contratista(lis):
    datos ={'Representante':'','Nombre':'','Cedula':''}

    


