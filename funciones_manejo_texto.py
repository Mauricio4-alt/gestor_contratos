def extraer_datos(lista,palabras):
    
    
    
    datos = {}
    long_lista = range(len(lista))
    for i in long_lista:
        if lista[i].lower() in palabras.keys() and lista[i].lower() != 'de':
            datos[lista[i]]= lista[i+1]
        
            
    return datos    
        
        
        







