import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\mjurdanetal\AppData\Local\Programs\Tesseract-OCR\tesseract'

def extraer_texto(img):
    # Leer la imagen desde la ruta especificada
    img = cv2.imread(f'C://gestor_contratos//contratos_convertidos//{img}.jpeg')
    
    # Convertir la imagen a escala de grises para mejorar el OCR
    custom_config = r'--oem 3 --psm 6'
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Aplicar OCR a la imagen en escala de grises
    text = pytesseract.image_to_string(img_gray,config=custom_config, lang='spa')
    
    return text
# print('text:',extraer_texto('contrato_1-1'))