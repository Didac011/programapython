'''31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.'''
frase = "A quién madruga Dios ayuda"
encontrar = input("Introduce la palabra que quieres buscar: ")
if encontrar in frase:
    indice = frase.find(encontrar)
    print ("La palabra se encuentra en la posición:", indice)
else:
    print("La palabra no se encuentra en la frase")