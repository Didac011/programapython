'''QUIERO QUE EL JUGADOR INTRODUZCA UN NUMERO DEL 1-5 Y EL ORDENADOR PIENSA OTRO NUMERO AL AZAR.'''
import random
var_random = random.randint(1,5)
var_usuario=int(input("introduce un número del 1 al 5: "))
if var_usuario>=1 or var_usuario<=5:
    if var_usuario!=var_random:
        print("fallaste")
    else:
        print("acertaste")
else:
    print("no has introducido el rango correcto")
#en clase plantee forzar que el usuario deba introducir el valor del 1-5 y no otro.

'''otra manera'''
import random
var_random = random.randint(1,5)
var_usuario=int(input("introduce un número del 1 al 5: "))
if var_usuario>=1 in "12345":
    if int(var_usuario)==var_random:
        print("fallaste")
    else:
        print("acertaste")
else:
    print("no has introducido el rango correcto")
#en clase plantee forzar que el usuario deba introducir el valor del 1-5 y no otro.