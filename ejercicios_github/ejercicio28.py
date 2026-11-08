'''Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.'''
respuesta=input("introduce una caracter: ")
if respuesta.isupper()==True:
    print("es mayúscula")
elif respuesta.islower()==True:
    print("es minúscula")
elif respuesta.isnumeric()==True:
    print("el valor es un número")
else:
    print("el valor es un caracter")