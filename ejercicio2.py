def calcular_factorial (n):
    factorial = 1
    for numero in range(1, n + 1):
        factorial *= numero 
    
    return factorial



n = 5

resultado = calcular_factorial(n)

print(resultado)

