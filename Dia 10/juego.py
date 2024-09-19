import pygame
import random
import math
from pygame import mixer
#Inciiar pygame
pygame.init()

#Dar medidas de la pantalla del juego
pantalla = pygame.display.set_mode((800,600))

#Titulo e Icono
pygame.display.set_caption("Invasion Espacial")
icono = pygame.image.load("planeta.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

#agregar musica
mixer.music.load('still DRE.mp3')
mixer.music.set_volume(0.5)
mixer.music.play(-1)

#crear jugador
img_jugador = pygame.image.load("jet.png")
jugador_x = 368
jugador_y = 530
jugador_x_cambio = 0

#Crear enemigo
img_enemig = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8 

for e in range(cantidad_enemigos):
    img_enemig.append(pygame.image.load("ovni.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(50)

#Crear bala
balas = []
img_bala = pygame.image.load("bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

#putaje 
puntaje = 0 
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def textoFinal():
    mi_fuente_final = fuente_final.render("JUEGO TERMINADO" , True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (100, 200))


#funcion mostrar puntaje
def mostrarPuntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

#Funcion posicion jugador
def jugador(x, y):
    pantalla.blit(img_jugador,(x, y))

#Funcion posicion jugador
def enemigo(x, y, ene):
    pantalla.blit(img_enemig[ene],(x, y))

#Funcion disparar bala
def dispararBala(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))
    
#Funcion detectar colisiones
def hayColisiones(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distancia < 27:
        return True
    else:
         return False

#loop juego
ejecutar = True
while ejecutar:
   
    #imagen de fondo
    pantalla.blit(fondo, (0,0))
    #iterar eventos
    for evento in pygame.event.get():
        #Cerrar programa "X"
        if evento.type == pygame.QUIT:
            ejecutar = False

        #Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            #presionar flecha izq
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.5
            #presionar flecha der
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                nueva_bala = {
                    "x": jugador_x,
                    "y": jugador_y,
                    "velocidad": -5
                }
                balas.append(nueva_bala)
        #Eveto soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or pygame.K_RIGHT :
                jugador_x_cambio = 0
    
    #modificar posicion jugador
    jugador_x += jugador_x_cambio
     
    #Mantener dentro de los bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    #modificar posicion enemigo
    for e in range(cantidad_enemigos):

        #fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]= 1000
            textoFinal()
            break
        enemigo_x[e] += enemigo_x_cambio[e]
    
    #Mantener dentro de los bordes enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]
        
        # colision
        for bala in balas:
            colision_bala_enemigo = hayColisiones(enemigo_x[e], enemigo_y[e], bala["x"], bala["y"])
            if colision_bala_enemigo:
                sonido_colision = mixer.Sound("explosion.mp3")
                sonido_colision.play()
                balas.remove(bala)
                puntaje += 1 
                enemigo_x[e] = random.randint(0, 736)
                enemigo_y[e] = random.randint(20, 200)
                break
        
        enemigo(enemigo_x[e], enemigo_y[e], e)
    

    #movimiento bala
    for bala in balas:
        bala["y"] += bala["velocidad"]
        pantalla.blit(img_bala, (bala["x"] + 16, bala["y"] + 10))
        if bala ["y"] < 0 :
            balas.remove(bala)

    jugador(jugador_x, jugador_y)
   
    #mostrar puntaje
    mostrarPuntaje(texto_x, texto_y)
    #Actualizar
    pygame.display.update()
    