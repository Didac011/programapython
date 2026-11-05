respuesta=input("introduce una letra: ")
if respuesta.isalpha()==True:
    if respuesta.isupper():
        print("es mayúscula")
    else:
        print("es minúscula")
else:
    print("el valor no es una letra")

'''otra manera'''

respuesta=input("introduce una letra: ")
if respuesta.isnumeric()==False:
    if respuesta.isupper():
        print("es mayúscula")
    else:
        print("es minúscula")
else:
    print("el valor no es una letra")