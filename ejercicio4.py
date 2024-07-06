def encontrar_mayor(numeros):
    mayor_Total = numeros[0]
    for numero in numeros:
        
        if mayor_Total < numero:
            mayor_Total = numero
        else:
            continue
        
    return mayor_Total



numeros = [10, 20, 5, 8, 30]

mayor = encontrar_mayor(numeros)
print(mayor)