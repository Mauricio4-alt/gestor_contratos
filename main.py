from __init__ import *

import aspose.words as aw


# Cargar archivo PDF
doc = aw.Document()
builder = aw.DocumentBuilder(doc)
builder.writeln("Hola Mauricio Jose")
doc.save(".\\out.txt")
