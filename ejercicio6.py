def calcular_promedio(numeros):
    total = 0
    for numero in numeros:
        total += numero
    promedios = total / len(numeros)

    return promedios


numeros = [10, 20, 30, 40, 50]
promedio = calcular_promedio(numeros)
print(promedio)