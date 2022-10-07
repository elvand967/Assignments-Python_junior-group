# Практическая работа № 01-1(PyGame)
# источник: https://younglinux.info/pygame/key
# Пусть в центре окна имеется круг, который можно двигать по горизонтали клавишами стрелок клавиатуры.
# Сделать так, чтобы круг с той же скоростью, т. е. постепенно, возвращался назад в исходную точку, когда клавиша отпускается.

import pygame
import sys

FPS = 60
W = 700  # ширина экрана
H = 700  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга
x = W // 2
y = H // 2
r = 25

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 3
    elif keys[pygame.K_RIGHT]:
        x += 3

    elif keys[pygame.K_UP]:
        y -= 3

    elif keys[pygame.K_DOWN]:
        y += 3


    clock.tick(FPS)