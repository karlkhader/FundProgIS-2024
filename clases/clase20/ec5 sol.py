# Contruyendo la descripción primero
def lee_peliculas1(fichero: str) -> list:
    
    f = open(fichero, encoding='utf8')
    
    listado_peliculas = []
    descripcion: str = ''
    for line in f:
        if line[0] == '*':
            if descripcion != '':
                pelicula: dict = {
                    'nombre': titulo,
                    'descripción': descripcion.strip()
                    }
                listado_peliculas.append(pelicula)
                
            titulo: str = line[1:].strip()
            descripcion: str = ''  
        else:
            descripcion += line
    
    pelicula = {
        'nombre': titulo,
        'descripción': descripcion
        }
    listado_peliculas.append(pelicula)
    
    return listado_peliculas

# Contruyendo la películoa y actualizando la descripción de la película anterior
def lee_películas2(nombre_fichero: str) -> list:
    pelis: list = []
    f = open(nombre_fichero, encoding="utf8")
    for l in f:
        l = l.strip()
        if l[0] == "*":
            d = {
                    "nombre": l[1:],
                    "descripción": ""
                }
            pelis.append(d)
        else:
            pelis[-1]["descripción"] += l + " "
    f.close()    
    return pelis

def busca_pelicula(pelis: list, nombre: str) -> str:
    descripción: str = ""
    i: int = 0
    while i < len(pelis) and pelis[i]["nombre"] != nombre:
        i += 1
    if i < len(pelis):
        descripción = pelis[i]["descripción"]
    
    return descripción

# Programa principal
peliculas: list = lee_películas1("cine2017.txt")
print(peliculas)
print(f"Coco: {busca_pelicula(peliculas, 'Coco')}")
print(f"Nemo: {busca_pelicula(peliculas, 'Nemo')}")