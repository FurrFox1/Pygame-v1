import pygame
import sys

# Colores

NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 128, 0)
AMARILLO = (255, 255, 0)
CELESTE = (0, 255, 255)
GRIS = (128, 128, 128)

# Ventana

ancho = 1000
largo = 768
SIZE = (ancho, largo)
VENTANA = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Super Sonic Survival")

ejecutando = True

# Reloj

clock = pygame.time.Clock()

# Listas

lista_obstaculos = []
lista_anillos = []
lista_powerup = []

# Característica personaje

pos_x = 30
pos_y = 500
personaje_alto = 100
personaje_ancho = 100
personaje_original_alto = 100  # Altura original del personaje
personaje = pygame.image.load("./Imagenes/Fly.png").convert()
personaje = pygame.transform.scale(personaje, (personaje_ancho, personaje_alto))
personaje.set_colorkey([255, 255, 255])

Vida = 50
max_tiempo = 0
tiempo_inicial = 0  # Inicializa el tiempo al comienzo

reproduciendo_musica = True
en_pausa = False
reiniciar = False


# Fondo y escalamiento

fondo = pygame.image.load("./Imagenes/fondo.png")
fondo = pygame.transform.scale(fondo, SIZE)
fondo_x = 0
fondo_velocidad = 20

# Archivo Maxscore
try:
    with open("./Maxscore.txt", "r") as file:
        max_tiempo = int(file.readline().strip())
except FileNotFoundError:
    with open("./Maxscore.txt", "w") as file:
        file.write("0")

# Evento personalizados

EVENT_NUEVO_ANILLO = pygame.USEREVENT + 1
pygame.time.set_timer(EVENT_NUEVO_ANILLO, 5000)

EVENT_NUEVO_OBSTACULO = pygame.USEREVENT + 2
pygame.time.set_timer(EVENT_NUEVO_OBSTACULO, 1000)

EVENT_NUEVO_POWERUP = pygame.USEREVENT + 1
pygame.time.set_timer(EVENT_NUEVO_POWERUP, 40000)


