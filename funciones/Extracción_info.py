import re

def extraer_drepresentante(texto,pa_representante,pa_cedula,pa_empre,pa_nit):
    datos ={'nombre_representante':'',
            'cedula_representante':'',
            'Empresa':'',
            'Nit':''
            }
    n_representante = re.compile(pa_representante,re.IGNORECASE)
    c_representante=re.compile(pa_cedula,re.IGNORECASE)
    empresa =re.compile(pa_empre,re.IGNORECASE)
    nit =re.compile(pa_nit,re.IGNORECASE)
    
    n_representante=n_representante.search(texto)
    c_representante=c_representante.search(texto)
    empresa = empresa.search(texto)
    nit = nit.search(texto)
    #info para el contratante
    # r'(?:entre los suscritos a saber )?([\w ]+)[,;.]? identificado con cédula'
    #r'(?:de ciudadanía no\. |de ciudadanía número )(\d{1,3}\.?\d{3}\.?\d{3})'
    #r'(?:representante legal de |representación de)([\w\. ]+)[,;]? ')
    #r'\d{3}\.\d{3}\.\d{3}[ ]?\-[ ]?\d'
    if n_representante:
        datos['nombre_representante']=n_representante.group(1)
    
    if c_representante:
        datos['cedula_representante']=c_representante.group(1)
    if empresa:    
        datos['Empresa']=empresa.group(1)
    if nit:
        datos['Nit']=nit.group(1) + '-' +nit.group(2)
    return datos,nit.end()
        
def extraer_cpuntuales(patron,paginas,funcion): # para garantizar el exito de esta expresión es necesario usar . en ella
    
    coincidencias = None  # Inicializamos la variable para evitar errores si no hay coincidencias

    for pagina in paginas:
        texto = funcion(pagina)
        resultado = re.search(patron, texto, re.DOTALL)  # Realizamos la búsqueda con el patrón
        if resultado:
            coincidencias = resultado.group(1)  # Tomamos el primer grupo coincidente
            break  # Detenemos el bucle si encontramos coincidencias
    return coincidencias


# def extraer_obligaciones(texto,patron):
#     match = re.search(texto,patron,re.IGNORECASE)
#     result = ""
#     if match:
#         result = match.group()
#     return result

    


    

    
    
    









        

