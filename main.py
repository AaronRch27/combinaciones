from itertools import combinations
valores = [
    21414749.07,
    88257099.82,
    69508686.31,
    85800705.39,
    2479697.59,
    6363659.47,
    4999376.96,
    826565.86,
    17312570.15,
    18805704.77,
    71998254.77,
    3611888.61,
    18811206.12,
    9674334.58,
    5912093.35,
    10749260.64,
    21415156.72,
    19112076.48,
    14561145.46,
    41946794.10,
    6572237.75,
    24111938.08,
    23109733.44,
    771067.40,
    771067.40]

cantidad = 118310294.81

            
# Función para encontrar combinaciones
def encontrar_combinaciones(valores, cantidad):
    for r in range(1, len(valores) + 1):
        for combinacion in combinations(valores, r):
            if round(sum(combinacion), 2) == cantidad:
                return combinacion
    return None

# Buscar combinaciones
resultado = encontrar_combinaciones(valores, cantidad)

if resultado:
    print("Combinación encontrada:", resultado)
else:
    print("No se encontró ninguna combinación.")
