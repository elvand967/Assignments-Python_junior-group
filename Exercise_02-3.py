# Задание № 02-3(PyGame)
# источник https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/19-animations.html
# Написать программу, в которой по нажатию клавиш будет двигаться квадрат размером 20х20 пикселей.
# Учесть, что квадрат не должен выходить за границы экрана.

import sys
import pygame

pygame.init()

WHITE = (255, 255, 255)

screen = pygame.display.set_mode((600, 600))
rect = pygame.Rect(50, 50, 20, 20)

fl_start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.move_ip(-20, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(20, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -20)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, 20)

    screen.fill(WHITE)
    pygame.draw.rect(screen, (0, 0, 255), rect, 0)

    pygame.display.flip()