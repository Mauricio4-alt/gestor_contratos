import pytesseract
from PyPDF2 import PdfReader,PdfWriter
from pdf2image import convert_from_path
from io import Bytes10

archivo_original =""
archivo_protegido =""
clave =""
def proteger_pdf_y_extraer_texto(archivo_original=archivo_original,archivo_protegido=archivo_protegido,clave=clave):
    #convertir el pdf a una lista de imagenes
    paginas =convert_from_path(archivo_original)
    pdf_protegido = PdfWriter()
    for num_pagina,imagen in enumerate(paginas):
        #aplicar OCR a las imagenes
        texto_extraido=pytesseract.image_to_string(imagen)
        print(f"texto extraido de la pagina {num_pagina + 1}")
        print(texto_extraido)
        imagen_en_bytes = Bytes10()
        imagen.save(imagen_en_bytes,format="PDF")
        imagen_en_bytes.seek(0)
        imagen_como_pdf =PdfReader(imagen_en_bytes)
        pdf_protegido.add_page((imagen_como_pdf[0]))
    pdf_protegido.encrypt(clave)

    with open(archivo_protegido,"wb")as archivo_protegido:
        pdf_protegido.write(archivo_protegido)