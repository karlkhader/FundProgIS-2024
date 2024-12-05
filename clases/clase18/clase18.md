# Clase 18: 04 de diciembre de 2024

Empezamos el tema de fichero y vemos qué alternativas tenemos para leer los ficheros.


## Ejercicio 1: Ficheros de números:
*Usando un editor de texto simple (tipo Notepad o incluso Thonny) cree un fichero con un número en cada línea. Realice un programa que lea el fichero e indique su suma.*

*Modifique el programa anterior para que nos indique su media.*

*Cree un fichero de texto donde hay muchas líneas y cada línea puede contener 1 o muchos números (separados por espacios). Realice un programa que lee el fichero y nos indique la media.*

[[Ver Código (1 número por línea)](t8e1.números1.py)]

[[Ver Código (varios número por línea)](t8e2.números2.py)]

## Ejercicio 2: Fichero de datos de series:

*Hacer un programa con una función que lea un fichero que tiene el siguiente formato:*
```
	Breaking Bad, 62, 50, Netflix
	Andor, 12, 45, Disney+
	La Casa del Dragón, 10, 55, HBOMax
	1899, 8, 50, Netflix
	The Boys, 24, 50, AmazonPrime
```
*La función debe devolverlo como lista de listas: `[ ["Breaking Bad", 62, 50, "Netflix"], ["Hawkeye", 6, 45, “Disney+"], …]`*
*La función debe devolver como lista de diccionarios: `[{"serie": "Breaking Bad", "episodios": 62, "duración": 50, "plataforma": "Netflix"}, …]`*
*En ambos casos añada un nuevo valor a cada una con la duración total. Luego, muestre el título de la más larga.*

[[Ver Código (Lista)](t8e3.series_listas.py)]

[[Ver Código (Diccionario)](t8e4.series_dict.py)]

## Ejercicio 3: Spotify

*En el fichero `songs.txt` tiene datos de las canciones más escuchadas de Spotify durante este año. De cada canción tenemos la siguiente información:*

* `'artist_names'`: *lista con los cantantes de la canción (list(str))*
* `'artist_names'`: *lista con los cantantes de la canción (list(str))*
* `'track_name'`: *nombre de la canción (str)*
* `'peak_rank'`: *posición más alta conseguida en el ranking semanal (int)*
* `'weeks_on_chart'`: *veces que ha estado en el ranking semanal (int)*
* `'danceability'`: *bailabilidad (float)*
* `'energy'`: *energía (float)*
* `'loudness'`: *ruidosidad (float)*
* `'speechiness'`: *cuánto se canta (cuanto más alto más palabras se dicen) (float)*
* `'liveness'`: *¿en vivo? (cuanto más alto más probabilidad hay) (float)*
* `'duration_ms'`: *duración (en milisegundos) (int)*

En la misma carpeta que `songs.txt` cree un nuevo fichero llamado `info_spotify.py` y añada al inicio:

```python
from json import load

f = open("songs.txt", encoding="utf-8")
SONGS = load(f)
f.close()
```

*Ese código carga en la variable `SONGS` todas las canciones (es una lista de canciones (diccionarios con la información indicada previamente)). Ahora en este fichero puede usar los datos y, por ejemplo: `print(SONGS[0]["artist_names"]` escribirá `['Glass Animals']` (que es el cantante de la primera canción).
Usando ese fichero, realice el código para contestar a las siguientes preguntas.*

1.	*¿Cuál es el título de la canción 79 del listado? (recuerde que las posiciones empiezan en 0)*
2.	*¿Cuál es el mejor puesto que ocupó en el ranking la última canción?*
3.	*¿Cuál es el segundo cantante de la segunda canción del listado?*
4.	*¿Cuántas canciones hay en el listado?*
5.	*¿Cuánto tiempo (en segundos y sin decimales) tardaríamos en escuchar todas las canciones?*
6.	*¿Cuántas canciones hay en vivo? (para considerarlas en vivo su liveness debe ser mayor de 0.6)*
7.	*¿Cuál es la energía media (con 2 decimales) de las canciones en las que participa ROSALÍA?*
8.	*¿Cuál es el título de la canción con más cantantes? ¿Cuántos cantantes participan? (En caso de que haya varias de igual número de cantantes elija la que esté antes)* 
9.	*¿Cuál es el título de la canción más corta? ¿Cuánto dura (en segundos sin decimales)? (En caso de que haya varias elija la última)* 

*Genere una lista de nombres de cantantes sin que haya repetidos.*

10.	*¿Cuántos artistas diferentes hay?*
11.	*¿Cuáles son los 10 últimos cantantes de esa lista? (genere un texto con sus nombres separados por ":-:").*

*Partiendo del listado previo, genere un diccionario donde para cada cantante (clave) indique cuántas canciones tiene (valor):*

12.	*¿Cuántas canciones hay de Imagine Dragons?*
13.	*¿Qué cantante tiene más canciones? ¿Cuántas tiene?* 


[[Ver canciones](songs.txt)]

[[Ver solución](info_spotify_completo.py)]
