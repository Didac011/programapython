'''20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10'''
num1= float(input("introduce un numero del 1 al 10: "))
num2= float(input("introduce otro numero del 1 al 10: "))
if num1 and num2 in [1,2,3,4,5,6,7,8,9,10]:
    if num1>num2:
        print("el primer número es más grande")
    elif num1<num2:
        print("el segundo es mayor que el primero")
    else:
        print("los dos números son iguales")
else:
    print("el rango no es correcto")