# def extraer_datos_contratante(texto):
#     # Texto de ejemplo
    

#     # Diccionario para almacenar los datos extraídos
#     datos_contratante = {}

#     # Extraer el nombre (asumimos que es el primer y segundo nombre/apellido al inicio del texto)
#     nombre_fin = texto.find("Identificado con")
#     nombre = texto[:nombre_fin].strip()

#     # Extraer la cédula
#     cedula_inicio = texto.find("cédula de ciudadanía No") + len("cédula de ciudadanía No ")
#     cedula_fin = texto.find(" de", cedula_inicio)
#     cedula = texto[cedula_inicio:cedula_fin].strip()

#     # Extraer el representante
#     representante_inicio = texto.find("representante Legal de") + len("representante Legal de ")
#     representante_fin = texto.find(".", representante_inicio)
#     representante = texto[representante_inicio:representante_fin].strip()

#     # Almacenar los datos en el diccionario
#     datos_contratante["nombre"] = nombre
#     datos_contratante["cedula"] = cedula
#     datos_contratante["representante"] = representante

#     # Imprimir los datos extraídos
#     return datos_contratante

        
        
            
            
            







