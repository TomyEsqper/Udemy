def suma_pares(numeros):
    pares  = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += numero
        else:
            continue
    return pares


numeros = [1, 2, 3, 4, 5, 6]

suma = suma_pares(numeros)
print(suma)
