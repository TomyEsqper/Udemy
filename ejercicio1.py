def contador_palabras (texto):
    palabras  = texto.split()
    diccionario = {}

    for palabra in palabras:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario



texto = "Hola como estás, Hola"


resultado = contador_palabras(texto)
print(resultado)