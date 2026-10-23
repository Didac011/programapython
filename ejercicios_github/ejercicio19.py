'''Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales''' 
num1= float(input("introduce un numero: "))
num2= float(input("introduce otro numero: "))
if num1>num2:
    print("el primer número es más grande")
elif num1<num2:
    print("el segundo es mayor que el primero")
else:
    print("los dos números son iguales")