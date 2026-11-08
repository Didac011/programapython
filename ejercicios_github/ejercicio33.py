'''33. Programa un código que permita contar el número de vocales de la siguiente frase: No hay mal que dure cien años '''
frase = "No hay mal que dure cien años"
vocales1 = "aá"
vocales2 = "eé"
vocales3 = "ií"
vocales4 = "oó"
vocales5 = "uú"
contador1 = 0
contador2 = 0
contador3 = 0
contador4 = 0
contador5 = 0

for caracter in frase:
    if caracter in vocales1: 
        contador1 += 1
    elif caracter in vocales2:
        contador2 += 1
    elif caracter in vocales3:
        contador3 += 1
    elif caracter in vocales4:
        contador4 += 1
    elif caracter in vocales5:
        contador5 += 1
print("El número de a es", contador1)
print("El número de e es", contador2)
print("El número de i es", contador3)
print("El número de o es", contador4)
print("El número de u es", contador5)