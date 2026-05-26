
# ============================================================
# Fundamentos de Programación - Grupo: 213022_72
# Fase 5 - Evaluación Final POA
# Problema 5: Control de horas semanales del equipo
# Nicol andrea julio zambrano
# ============================================================

# --- Datos Iniciales ---
# Matriz: [Nombre del Recurso, Lunes, Martes, Miércoles, Jueves, Viernes]
equipo = [
    ["Ana García",    9, 8, 10, 9, 8],
    ["Luisa Serpa", 7, 6,  8, 7, 6],
    ["Sara López",    8, 9,  9, 8, 9],
    ["Carlos Ruiz",   10, 9, 10, 9, 10]
]

UMBRAL_HORAS = 40  # Horas estándar semanales


# --- Módulo (función) ---
def calcular_jornada(recurso):
    """
    Recibe una fila de la matriz con el formato:
    [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]
    Retorna el total de horas y la clasificación de jornada.
    """
    nombre = recurso[0]
    horas_diarias = recurso[1:]  # Horas de lunes a viernes

    # Calcular suma total de horas semanales
    total_horas = 0
    for horas in horas_diarias:
        total_horas += horas

    # Clasificar la jornada
    if total_horas > UMBRAL_HORAS:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total_horas, clasificacion


# --- Programa Principal ---
print("=" * 55)
print("   INFORME DE HORAS SEMANALES DEL EQUIPO")
print("=" * 55)
print(f"{'Recurso':<18} {'Total Horas':^12} {'Clasificación':<15}")
print("-" * 55)

for recurso in equipo:
    nombre, total, clasificacion = calcular_jornada(recurso)
    print(f"{nombre:<18} {total:^12} {clasificacion:<15}")

print("=" * 55)
print(f"Umbral de horas estándar: {UMBRAL_HORAS} horas/semana")
print("=" * 55)