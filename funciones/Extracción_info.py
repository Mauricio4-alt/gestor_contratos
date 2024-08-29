import re
from funciones_ocr import extraer_texto

def extraer_dcontratante(texto):
    datos ={'nombre_representante':'',
            'cedula_representante':'',
            'Empresa':'',
            'Nit':''}
    n_representante = re.compile(r'(?:entre los suscritos a saber )?([\w ]+)[, ] identificad[ao]',re.IGNORECASE)
    
    c_representante=re.compile(r'(cédula de ciudadanía no\.|cédula de ciudadanía número) (\d{1,3}\.?\d{3}\.?\d{3}) de',re.IGNORECASE)
    
    empresa =re.compile(r'representante legal de ([\w\. ]+)[,;]|representacion de ([\w\. ]+)[,;]',re.IGNORECASE)
    nit =re.compile(r'identificada con nit (\d{3}\.\d{3}\.\d{3}-\d)',re.IGNORECASE)
    n_representante=n_representante.search(texto)
    c_representante=c_representante.search(texto)
    empresa = empresa.search(texto)
    nit = nit.search(texto)
    if n_representante:
        datos['nombre_representante']=n_representante.group(1)
    if c_representante:
        datos['cedula_representante']=c_representante.group(2)
    if empresa:
        datos['cedula_representante']=empresa.group(1)
    if empresa:    
        datos['Empresa']=empresa.group(1)
    if nit:
        datos['Nit']=nit.group(1)
    
    return datos
            
    
                                
    
                                
        
    
info_contrato= []
texto = extraer_texto("contrato_corto-1")
contrato=extraer_dcontratante(texto)
print(texto)
print(contrato)
     
    


    


