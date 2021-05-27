import gzip

# nombre del archivo que vamos a descomprimir
archivoGZ = "archivo.gz"

# texto
texto = "Este texto es el que se va a escribir en el archivo.gz"

# comprimir un archivo
with gzip.open(archivoGZ,'wt') as f:
    f.write(texto)
f.close()