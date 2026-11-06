'''27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla'''
respuesta=input("introduce una letra: ")
if respuesta.isnumeric()==False:
    if respuesta.isupper():
        print("es mayúscula")
    else:
        print("es minúscula")
else:
    print("el valor no es una letra")