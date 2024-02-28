# Definición 
entero = 42
flotante = 3.14
cadena = "Hola, soy un string"
booleano = True

# Concatenación de variables 
resultado_concatenacion = cadena + " " + str(entero) + " " + str(flotante) + " " + str(booleano)

""" Límites de los enteros y flotantes en Python (comentarios)
 - Los enteros en Python 3 son de precisión ilimitada, y el único límite práctico es la memoria disponible.
 - Los flotantes en Python siguen el estándar IEEE 754. Tienen una precisión limitada y pueden mostrar errores de redondeo en operaciones aritméticas.
"""
# Fórmula de la suma de los primeros n números pares
num = 5 
suma_pares = num * (num + 1)

# Impresión de los resultados
print("Concatenación:", resultado_concatenacion)
print("Suma de los primeros", num, "números pares:", suma_pares)
