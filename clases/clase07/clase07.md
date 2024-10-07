# Clase 7 (7 de octubre de 2024)

En esta clase se repasó la parte de condiciones, sentencias de selección y se empezó a trabajar con sentencias de repetición.

A continuación se muestran los códigos trabajados en clase o aquellos que se dejaron para que los intentase el alumnado.

Especialmente importante para la parte de bucles son los [ejercicios cortos finales](#ejercicios-cortos).

## Días por año:

*Realice un programa que lea el nombre de un mes (entero en minúsculas) y nos día la cantidad de días que tiene ese mes.*

Aunque podríamos hacer un if con 12 casos, realmente hay 3 posibles valores resultantes válidos y podemos agrupar las condiciones. También es recomendable usar primero las condiciones más cortas y dejar para el `else` la más larga ya que no hay que ponerla.

[[Ver Código](t3e12.meses.py)]

## Calculadora

*Realice un programa que actúe como una calculadora simple. Para ello debemos leer dos valores reales, que serán los operadores y una letra, operador. Las posibles operaciones permitidas son +, -, \* o /.*

*Como resultado debe dar el valor de evaluar la operación o ERROR si no fue posible realizarla.*

Es un ejemplo típico de sentencia de selección múltiple.

[[Ver Código](t3e13.calculadora.py)]

## Ecuación de segundo grado

*Modifique el ejemplo del principio del tema, para que como respuesta el programa indique cuántas soluciones reales tiene (0, 1, 2 o infinitas) y en caso de tener un número contable que indíquelas.*

*Antes de empezar a programar piense los posibles casos:*
* *Hay una situación en la que hay infinitas soluciones*
* *Hay dos situaciones en las que no hay solución (al menos real)*
* *Hay dos situaciones en las que solo hay una solución*
* *Hay una situación en las que hay dos soluciones diferentes*

*Lea los coeficientes y calcule el discriminante (b*b-4ac). Posteriormente use una sentencia de selección múltiple para identificar los casos (únalos cuando sea posible) y calcule las soluciones.*

En este caso no se desarrolló el código pero si se identificaron los casos correspondientes:
* Hay una situación en la que hay infinitas soluciones
    * Si a, b y c son 0
* Hay dos situaciones en las que no hay solución (al menos real)
    * Si el discriminante es negativo
    * Si a y b son 0 y c no lo es
* Hay dos situaciones en las que solo hay una solución
    * a es 0 y b no lo es
    * El discriminante es 0
* Hay una situación en las que hay dos soluciones diferentes
    * El discriminante es positivo y mayor que 0 y a no es 0

[[Ver Código](t3e14.numSolucionesEc2gr.py)]

## Escribir N "Hola Mundo!"

*Realice un programa que escriba N (siendo N leído de teclado) veces la frase "Hola Mundo!"*

Ejemplo usado para introducir el bucle `while`.

[[Ver Código](t3e15.holamundo.py)]

## Tabla del 7

*Realice un programa que escriba la tabla de multiplicar del 7.*

Otro ejemplo usado para introducir el bucle `while`.

[[Ver Código](t3e16.tabla7.py)]

## Ejercicios cortos

### Ejercicio 1
*Lee 20 números y nos diga cuántos 0s hay*

Un elemento importante a destacar en este ejercicio, es que realmente no nos interesan los números concretos que hemos leído hasta el momento si no hay variable que nos almacene un resumen (de la parte que nos interese) de todos esos valores. Es decir, no nos interesa saber si el usuario ha metido 0 1 3 5 0 2 sino que hemos leído 2 ceros. Por ello, tendremos una variable `contador_de_0s` que nos almacene ese valor mientras que los números leídos los podemos ir machacando. Este tipo de variable que resumen los datos contando los valores que cumplen cierta propiedad se denominan **contadores**.

[[Ver Código](t3e17.cortos1.py)]

### Ejercicio 2
*Lee 10 números y nos diga su suma*

Similar al ejercicio anterior pero en este caso no nos interesa contar, sino sumar (acumular) todos los valores. Estas variables se denominan **acumuladores**.

[[Ver Código](t3e18.cortos2.py)]

### Ejercicio 3
*Modifique el anterior para calcular la media de los números leídos*

Sabiendo la suma de los valores, calcular la media es bastante sencillo, ya que solo hay que dividir esa suma entre el número de valores (10).

[[Ver Código](t3e19.cortos3.py)]

### Ejercicio 4
*Lee 30 números y nos muestre cuántos números pares y cuántos impares hay*

Similar al primero de los cortos, pero ahora con dos contadores (uno para pares y otro para impares). Realmente el de impares podría deducirse del de pares.

[[Ver Código](t3e20.cortos4.py)]

### Ejercicio 5
*Modifique el anterior ejercicio para que en vez de leer 30 números, lea hasta que el número sea negativo.*

Este ejemplo es importante ya que añade el concepto de **lectura adelantada**. Esto ocurre cuando la condición del bucle depende de lo que leemos y entonces hay que leer un valor previo al bucle y nos obliga a un esquema similar al siguiente:

```python
x = input(...) # Leemos
while condicion_que_depende_de_x: # Evaluar la condición 
  Código # Cálculos 
  x = input(...) # Leemos de nuevo
```

[[Ver Código](t3e21.cortos5.py)]

### Ejercicio 6
*Modifique el 3 (media) para que acabe cuando leamos un 0*

En este caso como en el ejercicio anterior hay que emplear lectura adelantada. Además, como dividimos entre la cantidad de veces que leemos, hay que controlar si no se ha leído ningún valor correcto:

[[Ver solución](t3e22.cortos6.py)]

### Ejercicio 7
*Lee un texto de 20 letras (una a una) e indique si aparece una vocal o no.*

En este ejercicio necesitamos una variable de las llamada centinelas (o `flags`) que solo tiene dos valores, `True` si ha ocurrido un evento o `False` si no. Inicialmente la ponemos a falso ya que no se ha leído nada y cuando se detecte el evento (lectura de una vocal) la ponemos a cierto.

[[Ver solución](t3e23.cortos7.py)]


### Ejercicio 8
*Modifique el 7 para que lea a lo sumo 20 letras (cuanto sepa si hay debe parar).*

Una forma sencilla de resolver este ejercicio es añadiendo la condición de que no se haya leído ninguna vocal al bucle (ese valor está almacenado en la variable centinela `hay_vocales`).

[[Ver solución](t3e24.cortos8.py)]

### Ejercicio 9
*Hacer un programa que lea dos números pero deben ser diferentes. Si se leen dos números iguales se debe repetir la petición de valores tantas veces como sea
necesaria hasta que consigamos que sean diferentes.*

Este ejemplo es peculiar ya que la condición del bucle depende de los valores leídos y habría que hacer lectura adelantada, pero lo que ponemos como lectura adelantada y el contenido del bucle completo es igual. Para estos casos nos podemos ahorrar la lectura adelantada e inicializar las variables de forma que al inicio entre la primera vez.

[[Ver solución](t3e25.cortos9.py)]

### Ejercicio 10
*Lea número hasta encontrar uno positivo y muestre el mayor.*

Este ejercicio quizás es uno de los más complejos de estos cortos:
* Necesitamos lectura adelantada (hay que leer mientras el valor sea negativo).
* Necesitamos una variable para almacenar el mayor leído hasta el momento (variable `mayor`).
* Esta variable se actualiza si leemos una mayor (`if mayor < n: mayor = n`).
* El valor inicial de la variable debe ser el primer valor leido (la lectura adelantada).

[[Ver solución](t3e26.cortos10.py)]