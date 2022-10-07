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
n = 3 # шаг смещения
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# координаты и радиус круга (стартуем с серидины виджета)
X = x = W // 2 # X - исходные  x - фактические
Y = y = H // 2
r = 20

def up_circle():
    sc.fill(WHITE)  # "удаляем следы" - очищаем виджет, задаем цвет фона
    pygame.draw.circle(sc, BLUE, (x, y), r)  # создаем новую фигуру (шар)
    pygame.display.update()  # Функции update() и flip() модуля display обновляют содержимое окна игры.
    # Это значит, что каждому пикселю заново устанавливается цвет.
    # Ограничение количества кадров в секунду, благодаря чему становится
    clock.tick(FPS) # проще просчитывать анимации и синхронизировать события

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT,
                         pygame.K_RIGHT,
                         pygame.K_UP,
                         pygame.K_DOWN]:
                while x != X or y !=Y:
                    if x != X:
                        if x > X:
                            x -= n
                        else:
                            x += n

                    if y != Y:
                        if y > Y:
                            y -= n
                        else:
                            y += n

                    up_circle()# Функция up_circle() обновляет содержимое окна игры при возрате шара.

    keys = pygame.key.get_pressed() # нажатие и удержание клавиши

    if keys[pygame.K_LEFT]:
        x -= n
    elif keys[pygame.K_RIGHT]:
        x += n

    elif keys[pygame.K_UP]:
        y -= n

    elif keys[pygame.K_DOWN]:
        y += n

    up_circle()  # Функция up_circle() обновляет содержимое окна игры + обеспечивает .

