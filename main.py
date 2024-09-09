from __init__ import *

# Cargar archivo PDF

paginas = list_pages('contrato_corto-*.jpeg')
texto = ""
for i in range(1,len(paginas)+1):
    texto += extraer_texto(f"contrato_corto-{i}")
# print(texto)






contrato = {}
# print(paginas)

# print(texto)

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
print(texto)
# Expresiones regulares para el contratist
# nombre = ' y por la otra ([áéíóúa-z ]+), identificado'
# empresa = r'(?:representante legal de la sociedad )?([\w\. ]*), sociedad'
# datos_contratista,fin = extraer_drepresentante(texto,nombre,cedula,empresa,nit)
# texto = texto[fin:]
# print(texto)
#delimitación del texto
# contrato['contratista'] = datos_contratista# print(sig_texto)

# extraer objeto del contrato
objeto = r'1\. OBJETO \. j ! (.)+2\. VIGENCIA'
contrato['objeto'] = extraer_cpuntuales(objeto,texto)

# extraer vigencia del contrato
# vigencia = r"2\. vigencia: (.*?)(?:3\. cláusulas|$)"
# contrato['objeto']= extraer_cpuntuales(vigencia,paginas,extraer_texto)



# for key,value in contrato.items():
    # print(f'{key} {value} ')
for element in contrato:
    print(f'{element}: {contrato[element]}')