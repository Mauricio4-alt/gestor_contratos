import re
from funciones_ocr import extraer_texto

def extraer_dcontratante(texto):
    datos ={'nombre_representante':'',
            'cedula_representante':'',
            'Empresa':'',
            'Nit':''
            }
    n_representante = re.compile(r'(?:entre los suscritos a saber )?([\w ]+)[,;.]? identificado con cédula',re.IGNORECASE)
    c_representante=re.compile(r'(?:de ciudadanía no\. |de ciudadanía número )(\d{1,3}\.?\d{3}\.?\d{3})',re.IGNORECASE)
    empresa =re.compile(r'(?:representante legal de |representación de)([\w\. ]+)[,;]? ',re.IGNORECASE)
    nit =re.compile(r'\d{3}\.\d{3}\.\d{3}[ ]?\-[ ]?\d',re.IGNORECASE)
    
    n_representante=n_representante.search(texto)
    c_representante=c_representante.search(texto)
    empresa = empresa.search(texto)
    nit = nit.search(texto)
    
    if n_representante:
        datos['nombre_representante']=n_representante.group(1)
    if c_representante:
        datos['cedula_representante']=c_representante.group(1)
    if empresa:    
        datos['Empresa']=empresa.group(1)
    if nit:
        datos['Nit']=nit.group()
    return datos
        
def extraer_dcontratista(texto):
    datos ={'nombre_representante':'',
            'cedula_representante':'',
            'Empresa':'',
            'Nit':''
            }
    
    
    n_representante = re.compile(r'(?: y por la otra |[\;] e )([\w ]+)[\n\ ,] ',re.IGNORECASE)
    
    # c_representante=re.compile(r'(?:de ciudadanía no\. |de ciudadanía número )(\d{1,3}\.?\d{3}\.?\d{3})',re.IGNORECASE)
    # empresa =re.compile(r'(?:representante legal de |representación de)([\w\. ]+)[,;]? ',re.IGNORECASE)
    # nit =re.compile(r'\d{3}\.\d{3}\.\d{3}[ ]?\-[ ]?\d',re.IGNORECASE)
    
    n_representante=n_representante.search(texto)
    # c_representante=c_representante.search(texto)
    # empresa = empresa.search(texto)
    # nit = nit.search(texto)
    
    
    if n_representante:
        datos['nombre_representante']=n_representante.group(1)
    # if c_representante:
    #     datos['cedula_representante']=c_representante.group(1)
    # if empresa:    
    #     datos['Empresa']=empresa.group(1)
    # if nit:
    #     datos['Nit']=nit.group()
    return datos
    
    
    
    
    
            
    
# texto = extraer_texto("contrato_corto-1")
texto = extraer_texto("contrato_1-1")
contrato=extraer_dcontratista(texto)    
print(texto)
print(contrato)
