'''Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo'''
import math
valor_a = int(input("introduce el valor a de la equación: "))
valor_b = int(input("introduce el valor b de la equación: "))
valor_c = int(input("introduce el valor c de la equación: "))
discriminante = valor_b**2-4*valor_a*valor_c
if discriminante >=0:
    valor_raiz = math.sqrt(discriminante)
    x1 = (-valor_b + valor_raiz)/(2*valor_a)
    x2 = (-valor_b - valor_raiz)/(2*valor_a)
    print("El valor de la raíz cuadrada es: ", valor_raiz)
    print("Las soluciones son: ", x1, " y ", x2)
else:
    print("El valor de la raíz cuadrada es negativo, no se puede calcular")