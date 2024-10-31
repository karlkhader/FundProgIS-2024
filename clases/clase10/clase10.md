# Clase 10: 30 de octubre de 2024

En esta clase comenzamos con el Tema 4, donde se introdujo la necesidad de dividir el código en pequeños trozos para facilitar su escritura y su reutilización. También vimos cómo se hacen y se usan funciones en python. Como ejemplo para ilustrar todo esto vimos el cálculo de un número combinatorio


## Ejemplo: Números combinatorios

La idea es hacer el cálculo de un número combinatorio que es la división entre m! y n!\*(m-n)! Como se observa se necesitan calcular 3 veces el factorial de diferentes valores y entonces crear una trozo de código que lo calcule y lo podamos reutilizar facilita mucho realizar el programa.

[[Ver código sin funciones](t4e01.combinatorio1.py)]

[[Ver código con funciones](t4e02.combinatorio2.py)]



## Máximo Común Divisor

Dada la función del lateral realice las siguientes llamadas:
*a)Escribir por pantalla el MCD de 20 y 6
b)Escribir por pantalla el MCD de dos números leídos por teclado
c)Escribir por pantalla el triple del MCD de dos números leídos de teclado
d)Leer dos valores de teclado, n1 y n2, y calcular el MCD de n1+n2 y n1\*n2 (el valor se guardará en otra variable).
e)Leer dos valores de teclado, n1 y n2, y asignar a n1 el valor de n1\*(n2/MCD(n1,n2)) y a n2 asignar el valor de n2\*(n1/MCD(n1,n2)).
f)Compruebe si el MCD(n1,n2) es igual al MCD(n2,n1), en caso de ser cierto debe escribir "El orden de los factores no altera el producto" y si es falso "Debo revisar el código, nunca debí llegar aquí".*

[[Solución](t4e03.mcd.py)]


## Cilindro 

*Realice dos funciones, una que calcule el área a partir del radio del círculo y otra que calcule su longitud.*

*Realice una función que calcule el área de un rectángulo.*

*Realice otra función que calcule el área del cilindro a partir de su radio y su altura. El área de un cilindro es la suma de sus componentes, es decir, es 2 veces área de la base (círculo) más el área del rectángulo.*

*Realice el programa principal que lea el radio y la altura del cilindro y nos muestre su área.*

[[Solución](t4e04.cilindro.py)]