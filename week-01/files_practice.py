# Ejercicio 4: Trabajar con archivos de texto

print("=== Ejercicio 4: Archivos ===")

# Parte 1: Crear y escribir archivo
print("\n1. Creando archivo...")

tecnologias = ["Python", "Git", "Flask", "NumPy", "Pandas", "Scikit-learn"]

# Escribir lista en archivo (cada elemento en una línea)
with open("week-01/tecnologias.txt", "w", encoding="utf-8") as archivo:
    for tech in tecnologias:
        archivo.write(tech + "\n")

print("✅ Archivo 'tecnologias.txt' creado")


# Parte 2: Leer archivo completo
print("\n2. Leyendo archivo completo...")

with open("week-01/tecnologias.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)


# Parte 3: Leer archivo línea por línea
print("\n3. Leyendo línea por línea...")

with open("week-01/tecnologias.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for i, linea in enumerate(lineas, 1):
        print(f"  {i}. {linea.strip()}")


# Parte 4: Agregar contenido al archivo (append)
print("\n4. Agregando nuevas tecnologías...")

nuevas_tech = ["TensorFlow", "PyTorch"]

with open("week-01/tecnologias.txt", "a", encoding="utf-8") as archivo:
    for tech in nuevas_tech:
        archivo.write(tech + "\n")

print("✅ Tecnologías agregadas")


# Parte 5: Verificar contenido actualizado
print("\n5. Contenido final del archivo:")

with open("week-01/tecnologias.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        print(f"  - {linea.strip()}")