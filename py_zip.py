import zipfile

# cargamos un archivo como clase zip
archivoZ = zipfile.ZipFile("archivo.zip")

# Listado de los archivos dentro del zip
archivoZ.namelist()

# Extraer un archivo del zip
archivoZ.extract("File")

# Extraer todos los archivos del zip
archivoZ.extractall()

# Guardar un archivo en un zip
archivoZ.write("File", compress_type=zipfile.ZIP_DEFLATED)

# Cerramos el archivo
archivoZ.close()