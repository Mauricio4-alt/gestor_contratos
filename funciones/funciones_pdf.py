from PyPDF2 import PdfReader 

def pdf_to_text(doc):
    
    # text = ""
    contrato = PdfReader(doc)
    pages = contrato.pages[1]
    texto = pages.extract_text()
    return texto
    



