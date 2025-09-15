import random

alumnos = [
    "Valentina De Los ángeles Albizú",
    "Pablo Andres Allende",
    "Luca Valentín Argumedo",
    "Pablo Avalos",
    "Lucas Avila",
    "Santino Barone",
    "Sofia Blangetti",
    "Nicolás Bohm",
    "Renzo Valentino Borello Canizo",
    "Juan Manuel Carrillo Taglio",
    "Facundo Gustavo Chacon Catalan",
    "Agustin Emiliano Contardi",
    "Jeronimo Coronel Alvarez",
    "Gabriel Emiliano Denis",
    "Facundo Gustavo Deseff",
    "Juan Martin García",
    "Enzo Giaquinta",
    "Sabrina Gimenez",
    "Joaquin Godoy",
    "Lucas Facundo Godoy",
    "Santino Alejo Godoy Galdeano",
    "Valentina Antonela Gordillo Moreno",
    "Lautaro Agustin Guardatti Esquivel",
    "Tiago Nahuel Guillot Duran",
    "Mateo Lautaro Liendo",
    "Juan Ignacio Martinez Quiroga",
    "Maximo Exequiel Monardez",
    "Tomas Agustin Mora Gonzalez",
    "Pablo Isaias Morinigo Lima",
    "Ares Martín Ocaña Martinez",
    "Thiago Santino Oviedo Saldaño",
    "Amanda Lucrecia Pagano",
    "Máximo Juan Cruz Quiroga",
    "Facundo Agustín Ramírez García",
    "Franco Agustin Rios Alzamora",
    "Leonel Enrique Rojas",
    "Matias Nicolas Ruiz Vargas",
    "Ramiro Ezequiel Salcedo",
    "Ismael Saleme Padolsky",
    "Ignacio Exequiel Sanchez",
    "Fabrizio Jonathan Simon Santos",
    "Cristian Gabriel Soto",
    "Giovanna Mercedes Suarez",
    "Ismael Mauricio Suarez",
    "Fernando Agustín Torrez",
    "Luca Nicolas Valdez",
    "Tiziano Ignacio Valentini",
    "Matias Nicolas Vargas",
    "Juan Ignacio Videla Continella",
    "Pablo Exequiel Avalos"
]

tam_alumnos = 4
grupos = []

while alumnos:
    fila = []
    for i in range(tam_alumnos):
        if alumnos:  # si todavía quedan
            elegido = random.choice(alumnos)
            alumnos.remove(elegido)
            fila.append(elegido)
    grupos.append(fila)   # 👈 ahora sí dentro del while

# Mostrar los grupos
for i, fila in enumerate(grupos):
    print(f"Grupo {i}:")
    for alumno in fila:
        print(f"  - {alumno}")
    print()
