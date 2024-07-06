from random import choice

# Mezcla palabras de la lista "palabrasAdivinar"
def palabraRandom(palabrasAdivinar):
    return choice(palabrasAdivinar)

def palabraEnGuiones(palabra):
    return ["_"] * len(palabra)

def mostrarPalabra(palabraGuiones):
    return " ".join(palabraGuiones)

def empezarJuego(palabraGuiones, palabra):
    contador = 6
    nombre = input("Ingrese su nombre: ")
    
    while contador > 0:
        print(f"""
              Esta es tu palabra:
                {mostrarPalabra(palabraGuiones)}
              """)
        letraJugador = input("\nIngrese una letra para adivinar la palabra: ").lower()
        
        
        if letraJugador in palabra:
            for i, char in enumerate(palabra):
                if char == letraJugador:
                    palabraGuiones[i] = letraJugador
        else:
            print("Su letra no se encuentra")
            contador -= 1   
        
        if "_" not in palabraGuiones:
            return f"¡Felicidades {nombre}, la palabra era {palabra}!"
    
    return f"Lo siento, tu palabra era {palabra}"        

# Lista de palabras para adivinar
palabrasAdivinar = [
    "elefante", "mariposa", "biblioteca", "helicoptero", "astronauta", 
    "chocolate", "dinosaurio", "estrella", "fantasma", "guitarra", 
    "hospital", "jirafa", "koala", "laberinto", "montana", 
    "naranja", "oceano", "pinguino", "chimenea", "robot"
]

# Iniciar el juego
primerPaso = palabraRandom(palabrasAdivinar)
segundoPaso = palabraEnGuiones(primerPaso)
ultimoPaso = empezarJuego(segundoPaso, primerPaso)
print(ultimoPaso)
