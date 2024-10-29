#Exercise2
#Conversion de unidades: Crea un programa que convierta una medida en metros a centimetros y milimetros. El programa debe pedir
#al usuario que ingrese una longitud en metros y luego mostrar el resultado en las dos unidades.

unidad = float(input("Ingrese el valor a convertir: "))

centimetros = unidad * 100
milimetros = unidad * 1000

print(f"Metros = {unidad}")
print(f"Centimetros = {centimetros}")
print(f"Milimetros = {milimetros} ")

#Exercise3
#Comparador de numeros: Escribe un programa que solicite dos numeros a un usuario y determine si el primer numero es mayor,
#menor o igual al segundo. Muestra el resultado en pantalla usando operadores relacionales.

number1 = float(input("Ingrese el primer numero: "))
number2 = float(input("Ingrese el segundo numero: "))

mayor = number1 > number2
menor = number1 < number2
igual = number1 == number2

print(f"¿El primer numero es mayor que el segundo? : {mayor}")
print(f"¿El primer numero es menor que el segundo?: {menor}")
print(f"¿Los numeros son iguales?: {igual}")

#Exercise4
#Verificación de edad: Crea un programa que pida la edad del usuario y verifique si es mayor de edad(18 años o mas). Usa
#operadores logicos para determinar si la persona puede votar o no.

verificación = int(input("Ingrese su edad: "))

adulto = verificación >= 18
noEsAdulto = verificación < 18


print(f"¿Puede votar?: {adulto} ")
print(f"¿No puede votar?: {not adulto}")








