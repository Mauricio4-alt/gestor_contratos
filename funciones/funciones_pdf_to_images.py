from pdf2image import convert_from_path # funciones para manipular pdfs
from pathlib import Path as path # gestor de rutas desde python
import os # comunicación de python con el sistema operativo


# Ruta del ejecutable de Poppler
poppler_path = r'C:\Program Files\poppler-24.07.0\Library\bin' # binarios de popler para el correcto funcionamiento del programa
save_folder = path(r"C:\gestor_contratos\contratos_convertidos") #fichero destino

def pdf_to_images(document_path, poppler_path=poppler_path):
    # Ruta completa al archivo PDF
    root = path(f'C://gestor_contratos//contratos//{document_path}.pdf') # se crea un objeto root
    root = str(root) # root se vuelve una cadena para cuando los solicite convert_from_path
    # Convertir PDF a imágenes
    images = convert_from_path(root, poppler_path=poppler_path) # creamos un listado de imágenes y le asignamos la ruta popler
    return images # devolvemos dicho listado
#guardar imagenes
def save_images(images, document_name, save_folder=save_folder):
    # Crear la carpeta si no existe
    os.makedirs(save_folder, exist_ok=True)
    # proceso de guardar imágenes
    c = 1
    for image in images: #recorremos el listado de imagenes
        img_name = f'{document_name}-{c}.jpeg' #asignamos el nombre de la hoja del  contrato
        image.save(save_folder / img_name, "JPEG") # guardamos la imagen con el nuevo nombre [img_name ] en el fichero [saver folder]
        c += 1


