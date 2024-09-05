from __init__ import *

# Cargar archivo PDF
# texto = extraer_texto("contrato_corto-1")
texto = extraer_texto("contrato_2-1")
# print(texto)
contrato = {}

# Expresiones regulares para el contratante
nombre = r'(?:entre los suscritos a saber)?([áéíóúa-z ]+)(?>[, ]*identificad[ao])'
cedula = r'(?:de ciudadanía número |de ciudadanía no\. |de ciudadanía )([\d\.]*)'
empresa = r'(?:representación de| representante legal de )([\w\. ]+)[,;]?'
nit = r'identificada con (?:el )?NIT[:\s]+([\d\.]+)\s*[—\-–]\s*(\d)'

# Extraer datos del contratante y el ultimo punto de lectura
datos_contratante,fin = extraer_drepresentante(texto, nombre, cedula, empresa, nit)
contrato['contratante']= datos_contratante

# Delimitación del texto para evitar repeticiones
texto = texto[fin:]
# Expresiones regulares para el contratist
nombre = r'(?:y por la otra| e) ([áéíóúa-z ]+)'
empresa = r'(?:representante legal de la sociedad )?([\w\. ]*), sociedad'
datos_contratista,fin = extraer_drepresentante(texto,nombre,cedula,empresa,nit)
texto = texto[fin:]
# print(texto)
#delimitación del texto

contrato['contratista'] = datos_contratista# print(sig_texto)

# Extraer objeto
# pobj = r"\d+\.\s(.*?)(?=\s\d+\.\s|$)"
# obj=extraer_objcontrato(texto,pobj)
# print(texto)
# print(obj)
# contrato['Objeto'] = obj
# print(fin)

# extraer detalles financieros  
# contratista
# pa_contratante = r''
# contrato['obligaciones'] = dict()
# contrato['obligaciones']['contratista'] = extraer_obligaciones()



for i in contrato:
    print(f'{i}: {contrato[i]}')
