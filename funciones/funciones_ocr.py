import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mjurdanetal\AppData\Local\Programs\Tesseract-OCR\tesseract'

def extraer_texto(img):
    img = cv2.imread(f'C://gestor_contratos//contratos_convertidos//{img}.jpeg')

    text = pytesseract.image_to_string(img,lang='spa')
    return text

print('text:',extraer_texto('contrato_1-1'))