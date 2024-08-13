from __init__ import *


contrato = pdf_to_text('./contrato.pdf')


# extraemos datos del contratante

datos_contratante = extraer_datos_contratante(contrato)






print(datos_contratante)
