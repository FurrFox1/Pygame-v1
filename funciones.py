import pygame
import sys
import random
from config import *


def detectar_colision(rect, obstaculos):
    """
    Detecta colisiones entre un rectángulo y una lista de obstáculos.

    Args:
        rect (pygame.Rect): El rectángulo con el que se verifica la colisión.
        obstaculos (list): Una lista de rectángulos que representan obstáculos.

    Returns:
        bool: True si hay colisión, False de lo contrario.
    """
    for obstaculo in obstaculos:
        obstaculo_rect = pygame.Rect(
            obstaculo[0], obstaculo[1], obstaculo[2], obstaculo[3])
        if rect.colliderect(obstaculo_rect):
            return True
    return False


def crear_obstaculo():
    """
    Crea un nuevo obstáculo y lo agrega a la lista de obstáculos.

    Returns:
        None
    """
    x = ancho + random.randint(0, largo)
    y = random.randint(0, largo)
    ancho_obstaculo = 40
    alto_obstaculo = 40
    velocidad_obstaculo = random.randint(5, 8)
    meteoro = pygame.image.load("./Imagenes/Meteor.png").convert()
    meteoro = pygame.transform.scale(meteoro, (ancho_obstaculo, alto_obstaculo))
    meteoro.set_colorkey([255, 255, 255])
    lista_obstaculos.append([x, y, ancho_obstaculo, alto_obstaculo, velocidad_obstaculo, meteoro])


def crear_anillos():
    """
    Crea un nuevo anillo y lo agrega a la lista de anillos.

    Returns:
        None
    """
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


def crear_powerup():
    """
    Crea un nuevo Power Up y lo agrega a la lista de Power Ups.

    Returns:
        None
    """
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


def pausa():
    """
    Pausa el juego hasta que el jugador presione 'C' para continuar.

    Returns:
        None
    """
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
    """
    Quita la pausa y restaura el fondo de la ventana.

    Returns:
        None
    """
    VENTANA.fill((255, 255, 255))  # Restaurar el fondo blanco
    pygame.display.flip()



def mostrar_texto(pantalla, size, texto, fuente, color_texto, color_fondo, posicion):
    """
    Muestra texto en la pantalla.

    Args:
        pantalla (pygame.Surface): La superficie de la pantalla donde se mostrará el texto.
        size (int): Tamaño de fuente.
        texto (str): El texto que se mostrará.
        fuente (str): El nombre del archivo de fuente (None para fuente predeterminada).
        color_texto (tuple): El color del texto en formato (R, G, B).
        color_fondo (tuple): El color de fondo en formato (R, G, B) (None para transparente).
        posicion (tuple): Coordenadas (x, y) donde se mostrará el texto.

    Returns:
        None
    """
    fuente_obj = pygame.font.Font(fuente, size)
    texto_obj = fuente_obj.render(texto, True, color_texto, color_fondo)
    rect_texto = texto_obj.get_rect()
    rect_texto.center = posicion
    pantalla.blit(texto_obj, rect_texto)


def mostrar_objetos(lista_objetos, velocidad_min, velocidad_max):
    """
    Muestra objetos en la pantalla y actualiza sus posiciones.

    Args:
        lista_objetos (list): Lista de objetos a mostrar.
        velocidad_min (int): Velocidad mínima de los objetos.
        velocidad_max (int): Velocidad máxima de los objetos.

    Returns:
        None
    """
    for objeto in lista_objetos:
        x, y, ancho_objeto, alto_objeto, velocidad_objeto, imagen_objeto = objeto
        VENTANA.blit(imagen_objeto, (x, y))
        x -= velocidad_objeto
        if x + ancho_objeto < 0:
            x = ancho + random.randint(0, largo)
            y = random.randint(0, largo)
            velocidad_objeto = random.randint(velocidad_min, velocidad_max)
        objeto[0] = x
        objeto[1] = y
        objeto[4] = velocidad_objeto






