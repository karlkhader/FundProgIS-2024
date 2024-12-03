# Clase 17: 02 de diciembre de 2024

En esta clase hemos revisado el concepto y uso de diccionario y hemos practicado sobretodo el tema de lista de diccionarios.

## Ejercicio 1: Frecuencias
* Hacer una función `def freqs(s)` de recibiendo un texto s, nos devuelva un diccionario indicando cada letra que aparece en el texto cuántas veces aparece. Por ejemplo: `freqs("las gafas")` daría `{'l': 1, 'a': 3, 's': 2, ' ': 1, 'g': 1, 'f': 1}`.

[[Ver código](t7e04.frecuencias.py)]

# Ejercicio 2: Pagos
*Dados las líneas de texto del lateral. Realice las siguientes funciones:*
```python
pagos = [
"pepe: 20",
"lola: 30",
"pepe: 10",
"juan: 40",
"lola: 20",
"luis: 20",
"ana: 30",
"eva: 34"]
```
* *Recibiendo las líneas del lateral devuelva un diccionario que tenga como clave los nombres y valor, lo pagado en total.*
* *Otra que calcule el gasto medio.*
* *Finalmente, otra que imprima para cada uno si está a la par o si debe pagar/recibir y la cuánto.*

[[Ver solución](t7e05.pagos.py)]



## Ejercicio 3: Blackjack

* Genere una baraja ordenada con las 40 cartas.
* Desordene la baraja (elija dos posiciones al azar de la baraja e intercámbielas, repita el proceso 2000 veces).
* Reparta una carta al usuario.
* El usuario tiene dos opciones: pedir carta o plantarse. Este proceso se repite hasta que se planta o hasta que los valores de sus cartas superan 21.
* Si se pasó de 21, ya ha perdido.
* Sino el ordenador empieza a sacar cartas para él hasta que su valor supera al usuario o hasta que se pasa de 21.
* Si el ordenador se pasa de 21, gana el jugador.
* Si el ordenador supera al jugador sin pasarse de 21, gana el ordenador.

[[Ver solución](t7e06.blackjack.py)]
