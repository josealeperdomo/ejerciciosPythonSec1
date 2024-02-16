# ------- Ejercicios seccion 1
        
#1 verificar si un numero es par o impar (usar un input)

numero = int(input('ingresa un numero: '))
print('el numero es par' if numero%2 == 0 else 'el numero no es par')


#2 clasificar una persona en una categoria de edad. Por ejemplo si es un nino si es un adolescente o si es una persona adulta

edad = int(input('ingrese su edad: '))
if edad < 13:
    print( 'usted es un niño')
elif edad < 18:
    print('usted es un adolescente')
else:
    print('usted es un adulto')

#3 evaluar una nota e imprimier el resultado: Por ejemplo: se recibe una nota con un input (20), y le decimos que letra fue su clasificacion (a,b,c,d,f)
    
nota = int(input('introduce la clasificación: '))

if nota > 20 or nota < 0:
    print('Las notas van del 0 al 20. ingrese un valor valido')
elif nota >= 18:
    print('Su nota expresada en letras es: A')
elif nota >= 15:
    print('Su nota expresada en letras es: B')
elif nota >= 10:
    print('Su nota expresada en letras es: C')
elif nota >= 5:
    print('Su nota expresada en letras es: D')
elif nota >= 0:
    print('Su nota expresada en letras es: E')

#4 Calcular el descuento en una tienda si el monto supera los 100$ aplicar un 10% de descuento. Por ejemplo se recibe un numero el monto de la compra. usar input.
    
precio = int(input('Introduzca el precio: '))
if precio > 100:
    descuento = (precio * 10) / 100
    precio -= descuento
    print(f'el precio con el 10% de descuento es {precio}')
else:
    print(f'el precio no aplica para descuento, sigue siendo: {precio}')

#5 Determinar el tipo de triangulo en base al numero de lados (Equilatero, Isosceles o Escaleno). Usar 3 input.

primerLado = int(input('introduzca el tamano del primer lado de su triangulo: '))
segundoLado = int(input('introduzca el tamano del segundo lado de su triangulo: '))
tercerLado = int(input('introduzca el tamano del tercer lado de su triangulo: '))

if primerLado == segundoLado == tercerLado:
    print('el triangulo es equilatero')
elif primerLado == segundoLado or segundoLado == tercerLado or primerLado == tercerLado:
    print('el triangulo es isosceles')
else:
    print('el triangulo es escaleno')

#6 convertit una cantidad de dolares a bolivares o viceversa (usar input)
    
cambio = int(input('Para cambiar de dolares a bolivares ingrese 1, para cambiar de bolivares a dolares ingrese 2: '))

if cambio == 1:
    cantidad = int(input('ingrese la cantidad de dolares: '))
    resultado = cantidad * 36,2737
    print(f'{cantidad}$ en bolivares es igual a {resultado}bs')
elif cambio == 2:
    cantidad = int(input('ingrese la cantidad de bolivares: '))
    resultado = cantidad / 36,2737
    print(f'{cantidad}bs en dolares es igual a {resultado}$')
else:
    print('introdujo un numero invalido')