def extraer_datos_contratante(lista,*palabras):
    def iterador(lista=lista):
        texto= dict(lista)
        datos = dict()
        for i,j in texto.items():
            if i in palabras:
                 datos[i]= j
            elif j in palabras:
                datos[j]=i
            else:
                None
            return datos
    return iterador    
        







