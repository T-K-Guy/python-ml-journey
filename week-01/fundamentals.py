# Ejercicio 1: Listas y loops
print("=== Ejercicio 1: Tecnologías ===")
tecnologias = ["Python", "Git", "Flask", "NumPy", "Pandas"]

# TODO: Escribe el código aquí para imprimir cada tecnología con su índice
# Pista: usa enumerate()
for i, tec in enumerate(tecnologias):
    print(f"{i}, {tec}")

# Ejercicio 2: Diccionarios
print("\n=== Ejercicio 2: Perfil ===")
mi_perfil = {
    "nombre": "Ángel Gabriel",
    "semestre": 6,
    "objetivo": "ML Developer",
    "tecnologia_favorita": "Python"
}

# TODO: Escribe el código aquí para imprimir cada clave y valor
# Pista: usa .items()
for parametro, valor in mi_perfil.items():
    print(f"{parametro}: {valor}")

# Ejercicio 3: Funciones
print("\n=== Ejercicio 3: Calculadora ===")

def analizar_numeros(numeros):
    # TODO: Completa esta función
    # Debe retornar un diccionario con suma, promedio, máximo y mínimo
    suma = sum(numeros)
    promedio = sum(numeros) / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)

    calculadora = {
        "suma": suma,
        "promedio": promedio,
        "maximo": maximo,
        "minimo": minimo,
    }

    return calculadora

# Prueba (descomenta cuando termines la función):
datos = [10, 25, 30, 15, 40]
resultado = analizar_numeros(datos)
print(f"Suma: {resultado['suma']}")
print(f"Promedio: {resultado['promedio']}")
print(f"Máximo: {resultado['maximo']}")
print(f"Mínimo: {resultado['minimo']}")