def filtrar_impares(numeros):
    impares = []
    for numero in numeros:
        if numero % 2 != 0:
            impares .append(numero)
        
    return impares

numeros = [1, 2, 3, 4, 5, 6]
impar = filtrar_impares(numeros)
print(impar)