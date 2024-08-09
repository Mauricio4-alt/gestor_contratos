import PyPDF2.PdfReader as PdfReader

def pdf_to_text(doc):
    
    text = ""
    contrato = PdfReader(doc)
    pages = contrato.pages
    text= list(map(lambda page:page.extract_text(),pages))
    return text
text = pdf_to_text("")
print(text)


