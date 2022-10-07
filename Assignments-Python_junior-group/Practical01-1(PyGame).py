# Практическая работа № 01-1(PyGame)
# источник: https://younglinux.info/pygame/key
# Пусть в центре окна имеется круг, который можно двигать по горизонтали клавишами стрелок клавиатуры.
# Сделать так, чтобы круг с той же скоростью, т. е. постепенно, возвращался назад в исходную точку, когда клавиша отпускается.

import pygame
import sys

FPS = 60
W = 500  # ширина экрана
H = 500  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга (стартуем с серидины виджета)
X = x = W // 2 # X - исходные  x - фактические
Y = y = H // 2
r = 20

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT,
                         pygame.K_RIGHT,
                         pygame.K_UP,
                         pygame.K_DOWN]:
                x = X
                y = Y

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

    # Ограничение количества кадров в секунду, благодаря чему становится
    clock.tick(FPS) # проще просчитывать анимации и синхронизировать события