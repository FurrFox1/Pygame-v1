import pygame
import sys
import random
from config import *

# Colisiones

def detectar_colision(rect, obstaculos):
    for obstaculo in obstaculos:
        obstaculo_rect = pygame.Rect(
            obstaculo[0], obstaculo[1], obstaculo[2], obstaculo[3])
        if rect.colliderect(obstaculo_rect):
            return True
    return False


# Obstáculos

def crear_obstaculo():
    # Iniciar fuera de la pantalla a la derecha
    x = ancho + random.randint(0, largo)
    y = random.randint(0, largo)
    ancho_obstaculo = 40
    alto_obstaculo = 40
    velocidad_obstaculo = random.randint(5, 8)
    meteoro = pygame.image.load("./Imagenes/Meteor.png").convert()
    meteoro = pygame.transform.scale(meteoro, (ancho_obstaculo, alto_obstaculo))
    meteoro.set_colorkey([255, 255, 255])
    lista_obstaculos.append([x, y, ancho_obstaculo, alto_obstaculo, velocidad_obstaculo, meteoro])
    

# Anillos

def crear_anillos():
    # Iniciar fuera de la pantalla a la derecha
    x = ancho + random.randint(0, 200)
    y = random.randint(100, largo - 200)
    ancho_anillo = 40
    alto_anillo = 40
    velocidad_anillo = random.randint(2, 8)
    anillo = pygame.image.load("./Imagenes/anillo.png").convert()
    anillo = pygame.transform.scale(anillo, (ancho_anillo, alto_anillo))
    anillo.set_colorkey([255, 255, 255])
    lista_anillos.append(
        [x, y, ancho_anillo, alto_anillo, velocidad_anillo, anillo])

# Power Up

def crear_powerup():
    # Iniciar fuera de la pantalla a la derecha
    x = ancho + random.randint(0, 200)
    y = random.randint(100, largo - 200)
    ancho_powerup = 40
    alto_powerup = 40
    velocidad_powerup = random.randint(9, 15)
    powerup = pygame.image.load("./Imagenes/powerup.png").convert()
    powerup = pygame.transform.scale(powerup, (ancho_powerup, alto_powerup))
    powerup.set_colorkey([255, 255, 255])
    lista_powerup.append(
        [x, y, ancho_powerup, alto_powerup, velocidad_powerup, powerup])
    


# Funciones de pausado
def pausa():
    en_pausa = True
    mostrar_texto(VENTANA, 64, "Presiona 'C' para reanudar", None, BLANCO, None, (ancho // 2, largo // 2))
    fondo_negro = pygame.Surface((ancho, largo))
    fondo_negro.fill((0, 0, 0))
    fondo_negro.set_alpha(128)  # Opacidad
    VENTANA.blit(fondo_negro, (0, 0))  
    pygame.display.flip()
    while en_pausa:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                en_pausa = False
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    en_pausa = False
                    


def quitar_pausa():
    VENTANA.fill((255, 255, 255))  # Restaurar el fondo blanco
    pygame.display.flip()


def mostrar_texto(pantalla, size, texto, fuente, color_texto, color_fondo, posicion):
    fuente_obj = pygame.font.Font(fuente, size)
    texto_obj = fuente_obj.render(texto, True, color_texto, color_fondo)
    rect_texto = texto_obj.get_rect()
    rect_texto.center = posicion
    pantalla.blit(texto_obj, rect_texto)

def mostrar_objetos(lista_objetos, velocidad_min, velocidad_max):
    for objeto in lista_objetos:
        x, y, ancho_objeto, alto_objeto, velocidad_objeto, imagen_objeto = objeto
        VENTANA.blit(imagen_objeto, (x, y))
        # Actualiza la posición según la velocidad individual
        x -= velocidad_objeto
        if x + ancho_objeto < 0:
            x = ancho + random.randint(0, largo)
            y = random.randint(0, largo)
            # Asigna una nueva velocidad aleatoria
            velocidad_objeto = random.randint(velocidad_min, velocidad_max)
        objeto[0] = x
        objeto[1] = y
        objeto[4] = velocidad_objeto






