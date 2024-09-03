from __init__ import *

# Cargar archivo PDF
# texto = extraer_texto("contrato_corto-1")
texto = extraer_texto("contrato_1-1")
# print(texto)
contrato = {}

# Expresiones regulares para el contratante
nombre = r'(?:entre los suscritos a saber)?([áéíóúa-z ]+)(?>[, ]*identificad[ao])'
cedula = r'(?:de ciudadanía número |de ciudadanía no\. |de ciudadanía )([\d\.]*)'
empresa = r'(?:representación de| representante legal de )([\w\. ]+)[,;]?'
nit = r'identificada con (?:el )?NIT[:\s]+([\d\.]+)\s*[—\-–]\s*(\d)'

# Extraer datos del contratante y el ultimo punto de lectura
datos_contratante = extraer_drepresentante(texto, nombre, cedula, empresa, nit)
contrato['contratante'], fin = datos_contratante

# Delimitación del texto para evitar repeticiones
sig_texto = texto[fin:]
print(sig_texto)

# Expresiones regulares para el contratist
nombre = r'(?:y por la otra| e) ([áéíóúa-z ]+)'
empresa = r'(?:representante legal de la sociedad )?([\w\. ]*), sociedad'
datos_contratista,fin = extraer_drepresentante(sig_texto,nombre,cedula,empresa,nit)

#delimitación del texto
sig_texto =texto[fin:]
contrato['contratista'] = datos_contratista

# Extraer objeto


print(fin)
for i in contrato:
    print(f'{i}: {contrato[i]}')
