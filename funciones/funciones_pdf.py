import PyPDF2
def read_pdf(document,num_page):
    doc= open(document)
    reader = PyPDF2.PdfReader(doc)
    page = reader.pages[num_page]
    text = page.extract_text()
    return text