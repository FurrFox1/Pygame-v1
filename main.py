import pygame
import sys
import random
from config import *
from funciones import *
pygame.init()

# Sonido

anillo_sonido = pygame.mixer.Sound("./Sonidos/ring.mp3")
meteoro_sonido = pygame.mixer.Sound("./Sonidos/damage.mp3")
powerup_sonido = pygame.mixer.Sound("./Sonidos/powerup.mp3")
perder_sonido = pygame.mixer.Sound("./Sonidos/dead.mp3")

# VENTANA DE INICIO

VENTANA.fill(NEGRO)
ventana_inicial = True
while ventana_inicial:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ventana_inicial = False
            ejecutando = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            ventana_inicial = False

    VENTANA.fill((0, 0, 0))  
    mostrar_texto(VENTANA, 80, "Super Sonic Survival", None, AMARILLO, None, (ancho // 2, largo // 2 - 100))
    mostrar_texto(VENTANA, 50, "Presiona 'Enter' para comenzar", None, BLANCO, None, (ancho // 2, largo // 2 + 100))
    pygame.display.flip()

pygame.mixer.music.load("./Sonidos/music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Crear los primeros objetos
for i in range(5):
    crear_obstaculo()

for i in range(5):
    crear_anillos()

for i in range(1):
    crear_powerup()

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

        if event.type == EVENT_NUEVO_ANILLO:
            crear_anillos()

        if event.type == EVENT_NUEVO_OBSTACULO:
            crear_obstaculo()

        if event.type == EVENT_NUEVO_POWERUP:
            crear_powerup()

    vel_x = 0
    vel_y = 0
    # CONTROLES
    botones = pygame.key.get_pressed()
    if botones[pygame.K_ESCAPE]:
        ejecutando = False
    if botones[pygame.K_LEFT]:
        vel_x = -7
    if botones[pygame.K_RIGHT]:
        vel_x = 7
    if botones[pygame.K_UP]:
        vel_y -= 7
    if botones[pygame.K_DOWN]:
        vel_y += 7

    if botones[pygame.K_m]:
        if reproduciendo_musica:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause
        reproduciendo_musica = not reproduciendo_musica

    # Pausa juego

    if en_pausa == False:
        tiempo_actual = pygame.time.get_ticks()
        segundos_transcurridos = (tiempo_actual - tiempo_inicial) // 1000

    if botones[pygame.K_p]:
        if reproduciendo_musica:
            pygame.mixer.music.pause()
        pausa()
        if reproduciendo_musica:
            quitar_pausa()
            pygame.mixer.music.unpause()


    VENTANA.fill((255, 255, 255))

    # Dibujar fondo
    VENTANA.blit(fondo, (fondo_x, 0))
    VENTANA.blit(fondo, (fondo_x + fondo.get_width(), 0))
    fondo_x -= fondo_velocidad
    if fondo_x <= -fondo.get_width():
        fondo_x = 0

    # Dibujar obstáculos (Meteoros)
    mostrar_objetos(lista_obstaculos, 2, 8)

    # Dibujar anillos
    mostrar_objetos(lista_anillos, 3, 8)

    # Dibujar Powerup
    mostrar_objetos(lista_powerup, 8, 8)

    # Limitar la posición eje x del personaje para que no sobresalga de la ventana
    if pos_x + vel_x < 0:
        pos_x = 0
    elif pos_x + vel_x + personaje_ancho > ancho:
        pos_x = ancho - personaje_ancho
    else:
        pos_x += vel_x

    # Limitar la posición eje y del personaje para que no sobresalga de la ventana
    if pos_y + vel_y < 0:
            pos_y = 0
    elif pos_y + vel_y + personaje_alto > largo:
            pos_y = largo - personaje_alto
    else:
            pos_y += vel_y

    

    # Colision
    personaje_rect = pygame.Rect(pos_x, pos_y, personaje_ancho, personaje_alto)
    if detectar_colision(personaje_rect, lista_obstaculos):
        Vida -= 1
        mostrar_texto(VENTANA, 48, f"Salud: {Vida}", None, BLANCO, None, (150, 30))
        meteoro_sonido.play()

    for anillo in lista_anillos:
        if detectar_colision(personaje_rect, [anillo]):
            lista_anillos.remove(anillo)
            Vida += 10
            mostrar_texto(VENTANA, 48, f"Salud: {Vida}", None, BLANCO, None, (150, 30))
            anillo_sonido.play()

    for powerup in lista_powerup:
        if detectar_colision(personaje_rect, [powerup]):
            lista_powerup.remove(powerup)
            lista_obstaculos.clear()
            powerup_sonido.play()
            for i in range(5):
                crear_obstaculo()
            # Destello blanco    
            VENTANA.fill((255, 255, 255))  
            pygame.display.flip()
            pygame.time.delay(100)  
        


    # Texto para el cronómetro
    mostrar_texto(VENTANA, 48, f"Tiempo: {segundos_transcurridos} s", None, BLANCO, None, (ancho - 200, 30))


    # Ventana de GAME OVER
    if Vida <= 0:
        meteoro_sonido.stop()
        perder_sonido.play()
        pygame.mixer.music.stop()
        mostrar_texto(VENTANA, 70, "Game Over", None, ROJO, None, (ancho // 2, largo // 2 - 50))

        tiempo_transcurrido = segundos_transcurridos
        # Actualiza max_tiempo si el tiempo transcurrido es mejor
        if tiempo_transcurrido > max_tiempo:
            max_tiempo = tiempo_transcurrido

        # Actualiza el archivo "maxscore" con el nuevo valor de max_tiempo
        with open("./Maxscore.txt", "w") as file:
            file.write(str(max_tiempo))

        mostrar_texto(VENTANA, 48, f"Tiempo: {tiempo_transcurrido} s", None, BLANCO, None, (ancho // 2, largo // 2 + 20 ))
        
        mostrar_texto(VENTANA, 48, f"Mejor tiempo: {max_tiempo} s", None, BLANCO, None, (ancho // 2, largo // 2 + 60))

        mostrar_texto(VENTANA, 55, "Presiona 'Enter' para jugar nuevamente", None, BLANCO, None, (ancho // 2, largo // 2 + 120))

        mostrar_texto(VENTANA, 48, "Presiona 'Escape' para salir del juego", None, BLANCO, None, (ancho // 2, largo // 2 + 160))

        pygame.display.flip()
        reiniciar = False

        # Post-Game over
        while not reiniciar:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.play()
                        reiniciar = True
                        Vida = 50
                        pos_x = 30
                        pos_y = 500
                        segundos_transcurridos = 0
                        tiempo_inicial = pygame.time.get_ticks()
                        lista_obstaculos.clear()
                        lista_anillos.clear()
                        lista_powerup.clear()
                        for i in range(5):
                            crear_obstaculo()
                        for i in range(5):
                            crear_anillos()
                        for i in range(1):
                            crear_powerup()
                        ejecutando = True
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                

                    

    # Cuadrado personaje
    pygame.draw.rect(VENTANA, ROJO, (pos_x, pos_y,personaje_ancho, personaje_alto), -1)

    # Actualizamos los elementos en pantalla
    mostrar_texto(VENTANA, 48, f"Tiempo: {segundos_transcurridos} s", None, BLANCO, None, (ancho - 200, 30))
    mostrar_texto(VENTANA, 48, f"Salud: {Vida}", None, BLANCO, None, (150, 30))
    VENTANA.blit(personaje, (pos_x, pos_y))
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
