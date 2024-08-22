from pdf2image import convert_from_path
import pytesseract
from pathlib import Path

# Ruta al archivo PDF
pdf_path = Path('../contratos/contrato_1.pdf')

# Ruta al archivo de salida
output_text_path = Path('../contratos/contrato_1_texto.txt')

# Verificar que el archivo PDF existe
if not pdf_path.is_file():
    print(f"El archivo PDF no se encuentra en la ruta: {pdf_path}")
else:
    # Convertir el PDF a imágenes
    pages = convert_from_path(pdf_path, 300)

    # Inicializar el texto completo
    full_text = ""

    # Procesar cada página
    for i, page in enumerate(pages):
        # Extraer texto de la imagen de la página usando pytesseract
        text = pytesseract.image_to_string(page)
        
        # Agregar el texto extraído al texto completo
        full_text += f"--- Página {i + 1} ---\n{text}\n\n"

    # Guardar el texto completo en un archivo de texto
    with output_text_path.open('w', encoding='utf-8') as file:
        file.write(full_text)

    print(f"Texto extraído guardado en {output_text_path}")
