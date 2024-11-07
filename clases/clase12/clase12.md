# Clase 12: 06 de noviembre de 2024

En esta clase repasamos los ejercicios de funciones, y se introdujo el concepto de lista: conjunto de valores accesibles por índice.

Se vio cómo se creaba y principalmente cómo acceder a los diferentes valores:

## Ejercicio de clase 1 (EC1)
*__Función:__ recibe un número que indica los grados centígrados y debe devolver los grados Kelvin (ºK = ºC + 273.15).*

*__Programa principal:__ lea los grados centígrados, llame a la función de conversión y posteriormente escriba los grados Kelvin.*

*__Objetivos:__ Utilización y definición de una función sencilla que recibe un único parámetro y devuelve un valor real. Dónde colocar las funciones.*

[[Ver código](EC1.py)]

## Ejercicio de clase 2 (EC2)
*__Función:__ recibe el precio de un objeto y el impuesto (en porcentaje) y nos devuelve cuál será el precio total a pagar con dicho impuesto agregado (recuerde que el importe total a pagar será precio*(1+impuesto/100)).*

*__Programa principal:__ lea el precio y el impuesto y llame de forma correcta a la función y muestre por pantalla el importe total.*

*__Objetivos:__ Utilización y definición de una función que recibe varios parámetros y devuelve un valor real.*

[[Ver código](EC2.py)]

## Ejercicio de clase 3 (EC3)

*__Función:__ recibe un único número y nos devuelve si el número es par o impar (un bool).*

*__Programa principal:__ Lea 10 números y nos indique al final cuántos números son pares (para comprobar si son pares utilice la función realizada).*

*__Objetivos:__ Funciones que devuelven un valor booleano.*

[[Ver código](EC3.py)]

## Ejercicio de clase 4 (EC4)
*__Función:__ no recibe nada, pero internamente lee números de teclado hasta leer un 0 y que nos devuelve el porcentaje de positivos leídos.*

*__Programa principal:__ Invoca a la función anterior y escriba por pantalla el porcentaje de números positivos leídos.*

*__Objetivos:__ Funciones que no reciben parámetros.*

[[Ver código](EC4.py)]

## Ejercicio de clase 5 (EC5)
*__Función:__ recibe un número X y escribe por pantalla todos los números entre 1 y X.*

*__Programa principal:__ lee un número y que invoque a la función anterior con el número leído.*

*__Objetivos:__ Funciones que no devuelvan nada. Dentro de la función no ponga return.*

[[Ver código](EC5.py)]

## Ejercicio de clase 6 (EC6)
*__Función 1:__ recibe el lado de un triángulo equilátero (triángulo con todos los lados iguales) y nos devuelva la altura del mismo (altura = lado*raiz_cuadrada(3)/2).*

*__Función 2:__ recibe el lado del triángulo y nos devuelva su área (área = lado*altura/2). Llame desde esta función a la anterior para calcular la altura.*

*__Programa principal:__ lee el lado del triángulo y nos muestre por pantalla el área.*

*__Objetivos:__ Funciones que utilizan otras funciones.*

[[Ver código](EC6.py)]

## Ejercicio de clase 7 (EC7)
*__Función:__ Realice un subprograma que reciba la temperatura en grados centígrados y nos la devuelva la temperatura en grados kelvin (K = C + 273.15) y grados farenheit (F = C*9/5 + 32).*

*__Programa principal:__ lea una temperatura y mostrar los grados kelvin y farenheit de esa temperatura.*

*__Objetivos:__ Funciones que devuelven varios valores.*

[[Ver código](EC7.py)]


## Ejercicio de acceso a listas (transparencia 5)

Se ofrecen múltiples formas de acceder a diferentes valores:

[[Ver código](t5e01.rangos.py)]

## Ejercicio de recorridos (I): Exite negativo
*Realice una función que compruebe si en una lista hay números negativos*

[[Ver código](t5e02.existe_negativo.py)]

## Ejercicio de recorridos (II): Mayor
*Realice otra función que calcule el mayor valor de una lista*

[[Ver código](t5e03.menor.py)]

## Ejercicio de recorridos (III): Posición del mayor
*Codifique una función que devuelva la posición que ocupa el mayor valor de una lista*

[[Ver código](t5e04.posición_menor.py)]

## Ejercicio de recorridos (IV): Posición de un valor dado
*Codifique una función que devuelva la posición que ocupa un valor dado dentro de una lista*

[[Ver código](t5e05.posición_valor.py)]