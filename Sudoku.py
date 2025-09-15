import random

tablero = [[random.randint(1, 4) for _ in range(4)] for _ in range(4)]\

for fila in tablero:
    print(fila)

def validar_fila(tablero, fila):
    numeros = tablero[fila] # Obtener los números de la fila
    if len(set(numeros)) == 4:
        return True
    else:
        return False

def validar_columna(tablero, columna):
    numeros = [tablero[fila][columna] for fila in range(4)] # Obtener los números de la columna
    if len(set(numeros)) == 4:
        return True
    else:
        return False

def validar_subcuadro(tablero, fila_inicio, col_inicio):
    numeros = []
    for i in range(fila_inicio, fila_inicio + 2):   # Obtener los números del subcuadro 2x2
        for j in range(col_inicio, col_inicio + 2):
            numeros.append(tablero[i][j])
    if len(set(numeros)) == 4:
        return True
    else:
        return False

def validar_sudoku(tablero):
    for i in range(4):
        if not validar_fila(tablero, i):
            return False
        if not validar_columna(tablero, i):
            return False
    for i in range(0, 4, 2):
        for j in range(0, 4, 2):
            if not validar_subcuadro(tablero, i, j):
                return False
    return True

print("Resultados de las validaciones: ")
print(validar_subcuadro(tablero, 0, 0))  # subcuadro arriba izquierda
print(validar_subcuadro(tablero, 0, 2))  # subcuadro arriba derecha
print(validar_subcuadro(tablero, 2, 0))  # subcuadro abajo izquierda
print(validar_subcuadro(tablero, 2, 2))  # subcuadro abajo derecha
print(validar_sudoku(tablero))  # Validar todo el tablero
