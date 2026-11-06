'''26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.'''
respuesta=input("introduce una letra: ")
if respuesta.isnumeric()==False:
    if respuesta.isupper():
        print("es mayúscula")
    else:
        print("es minúscula")
elif respuesta.isnumeric()==True:
    print("el valor no es una letra")
else:
    print("el valor no es una letra")