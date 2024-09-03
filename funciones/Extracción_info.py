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
    else: print()
    if c_representante:
        datos['cedula_representante']=c_representante.group(1)
    if empresa:    
        datos['Empresa']=empresa.group(1)
    if nit:
        datos['Nit']=nit.group(1) + '-' +nit.group(2)
    return datos,nit.end()
        



if __name__=='__main__':
    texto ='''CONTRATO DE PRESTACIÓN DE SERVICIOS DE CONSULTORÍA CELEBRADO
    CASALIMPIA Y SINERGY 8 LOWELLS. |

    ANTONIO LÓPEZ HAZ identificado con cédula de ciudadanía No. 19265969 de
    Bogota,actuando en calidad de Representante Legal de CASALIMPIA S.A. , sociedad
    legalmente constituida, identificada con NIT 860.010.451-1 debidamente facultada para
    contratar tal como consta en el Certificado de Existencia y Representación legal expedido por
    la Cámara de Comercio de Bogotá, documento el cual se adjunta al presente contrato, quien
    para los efectos del presente Contrato se denominará EL CONTRATANTE; e ISABEL RIOS
    ¡identificada con cédula de ciudadanía No. 38.289.032 de Honda, en su condición de
    Representante Legal de la sociedad SINERGY 8 LOWELLS, sociedad legalmente
    constituida, identificada con NIT 830.078.090-1 , con capacidad para contratar en nombre de
    su representada, que para los'efectos del presente Contrato se denominará EL
    CONTRATISTA; EL CONTRATANTE y EL CONTRATISTA en el clausulado'que a
    continuación se señala, individualmente considerados se denominará como la “Parte” y
    conjuntamente como las “Partes”; hemos acordado suscribir el presente contrato mercantil.de
    prestación de servicios de consultoría, el cual se regirá por las siguientes cláusulas y en lo no
    previsto en ellas por las normas del derecho civil y comercial vigentes para este tipo de
    contratos.'''

    print(texto.index(' 830.078.090-1'))

        

