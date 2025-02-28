import pygame

camera = pygame.Rect(0, 0, 0, 0)


def create_screen(width, height, title):
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode((width, height))
    camera.width = width
    camera.height = height
    return screen


def set_camera(x, y):
    camera.x = x
    camera.y = y


def set_camera_center(x, y):
    set_camera(x - camera.width // 2, y - camera.height // 2)
