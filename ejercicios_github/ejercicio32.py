'''32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para que no importe si la palabra introducida está en mayúscula o minúscula.'''
frase = "A quién madruga Dios ayuda"
encontrar = input("Introduce la palabra que quieres buscar: ")
if encontrar.lower() in frase.lower():
    indice = frase.lower().find(encontrar.lower())
    print ("La palabra se encuentra en la posición:", indice)
else:
    print("La palabra no se encuentra en la frase")