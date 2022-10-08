# Задание № 02-3(PyGame)
# источник https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/19-animations.html
# Написать программу, в которой по нажатию клавиш будет двигаться квадрат размером 20х20 пикселей.
# Учесть, что квадрат не должен выходить за границы экрана.

import sys
import pygame

pygame.init()


FPS = 60
W = 500  # ширина экрана
H = 500  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
# определяем середину экрана виджета
X = x = W // 2 # X - исходные  x - фактические
Y = y = H // 2
xy = (x, y)# координаты верхнего-левого угла квадрата - ???
l = 20     # ширина прямоугольника (квадрата)
h = 20     # высота прямоугольника (квадрата)

screen = pygame.display.set_mode((W, H))
rect = pygame.Rect(x, y, l, h)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-l, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(l, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -h)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, h)

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, rect, 0)

    pygame.display.flip()