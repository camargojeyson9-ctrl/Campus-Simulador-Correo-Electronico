# Abrimos el archivo de texto
archivo = open("mbox.txt", "r", encoding="utf-8", errors="ignore")

# Creamos listas vacías para guardar la información
fechas_envio = []
autores = []
revisiones = []
archivos_modificados = []

# Leemos el archivo línea por línea
for linea in archivo:
  
  linea_limpia = linea.strip()

  # 1. Buscar las líneas de envío (empiezan con "From ")
  if linea.startswith("From "):
    fechas_envio.append(linea_limpia)

  # 2. Buscar los autores (empiezan con "Author: ")
  if linea.startswith("Author: "):
    # Quitamos la palabra "Author: " para quedarnos solo con el correo
    correo = linea.replace("Author: ", "").strip()
    autores.append(correo)

  # 3. Buscar las revisiones (empiezan con "New Revision: ")
  if linea.startswith("New Revision: "):
    rev = linea.replace("New Revision: ", "").strip()
    revisiones.append(rev)

  # 4. Buscar archivos modificados
  if linea_limpia.startswith("trunk/") or linea_limpia.startswith("branches/"):
    archivos_modificados.append(linea_limpia)

+archivo.close()



print("=== RESULTADOS ===")

print("1. Total de envíos encontrados:", len(fechas_envio))
print("Ejemplos:", fechas_envio[:2])

print("\n2. Total de autores encontrados:", len(autores))
print("Autores únicos:", set(autores))

print("\n3. Total de revisiones encontradas:", len(revisiones))
print("Primeras revisiones:", revisiones[:3])

print(
    "\n4. Total de archivos modificados encontrados:"
    f" {len(archivos_modificados)}"
)
print("Primeros archivos:", archivos_modificados[:3])