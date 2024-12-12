# Clase 19: 12 de diciembre de 2024

En esta clase propusimos varios ejercicios de examen:

## EC1 
*Una molécula química está representada por una lista de listas. Así la molécula H2SO4 estaría representada como: `sulfAcid = [[’H’, 2], [’S’, 1], [’O’, 4]]`. Hacer un subprograma para imprimir este tipo de listas. Por ejemplo `printChem(sulfAcid)` imprimiría `H2SO4`.*

[Ver código](printMolecula.py)

## EC2 
*Una cadena de caracteres contiene una suma sencilla de números de un sólo dígito (0 . . . 9). Hacer una función que recibiendo una de estas cadenas, devuelva el valor resultante de. Por ejemplo:*

```python
evalArit("8+9+1") #-> 18;
evalArit("9+0") #-> 9
```

[Ver código](evalArit.py)

## EC3 
*Dado un fichero cualquiera lleno de números enteros separados por comas, hacer una función que devuelva su media, su variación estándar y un diccionario con la frecuencia de cada uno. En el ejemplo dado en la siguiente página hay un ejemplo de números que son la salida de un dado aleatorio. Con este ejemplo nos debe salir:*

```python
stats(’dado.txt’) # (3.505, 1.6864744231382511, {1: 31, 2: 36, 3: 35, 5: 45, 6: 28, 4: 25})
```
Para calcular la desviación estándard usar la siguiente fórmula que no requiere calcular previamente la media. No meter los números en una lista. Hacer todos los cálculos con un solo bucle.

[Ver código](stat.py)

## EC4 
*Suponiendo que tenemos un fichero con el aspecto que se muestra en la siguiente página, hacer una función que nos devuelva un diccionario con las longevidades de cada filósofo. Sería: `leeEdades(’filosofos.txt’)` devolvería un diccionario así: `{’Heraclito de Efeso’: 60, ’Epicuro de Samos’: 71, ...}`. Los años que aparecen son AC (antes de Cristo).*


[Ver código](leeEdades.py)

## EC5 
*Repitiendo la función del lectura del problema 4, añadir una función que devuelva los nombres de los filósofos menos y más longevos del diccionario obtenido. Sería:*

```python
menosMasLong(dicFilos) # (’Empedocles de Agrigento’, ’Pitagoras de Samos’)
```

[Ver código](masLongevo.py)
