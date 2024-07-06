def es_palindromo(texto):
    invertido = texto [::-1]

    return texto == invertido
    


texto = "ana"

Resultado = es_palindromo(texto)
print(Resultado)