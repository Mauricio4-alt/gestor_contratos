from pdf2image import convert_from_path,convert_from_bytes
import pytesseract

pytesseract.tesseract_cmd = r'C:\Users\mjurdanetal\AppData\Local\Programs\Tesseract-OCR\tesseract'
# Ruta al archivo PDF
root ="C:\\gestor_contratos\\contratos\\contrato_1.pdf"
images = convert_from_path(root)

with open(root) as pdf:
    pdf = convert_from_bytes(pdf.read())