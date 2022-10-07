# Задание № 02-2(PyGame)
# источник https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/19-animations.html
# С помощью циклов, используя квадрат 10х10 пикселей и его след, нарисовать рамку 100х100 пикселей.
import pygame
import sys

FPS = 30 # зададим скорость обновления картинки в милесекундах
W = 200  # ширина экрана
H = 200  # высота экрана
WHITE = (255, 255, 255)
color1 = (0, 255, 0)
color2 = (255, 0, 0)
fl_color = True
square_color = color2
frame_side = 100 # длина стороны квадратной рамки
clock = pygame.time.Clock()

# координаты верхнего левого угла квадрата
X = x = 50 # X - исходные  x - фактические
Y = y = 50
l = 10      # длина стороны квадрата
fl_start = False
fl_RIGHT_DOWN = False

pygame.init()

screen = pygame.display.set_mode((W, H)) # экран виджета
screen.fill(WHITE) # покрасим наш экран в белый цвет

rectangle = pygame.Rect(x, y, l, l) # создадим исходный квадрат

flag_start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: # нажатие любой клавиши
            fl_start = True
            fl_RIGHT_DOWN = True


    if fl_start:
        if X + frame_side > x and fl_RIGHT_DOWN:
            rectangle.move_ip(l, 0)
            x += l
            #print(f'X {X}  x {x}\t | Y {Y}  y {y} fl_RIGHT_DOWN {fl_RIGHT_DOWN}; вправо')
        elif Y + frame_side > y and fl_RIGHT_DOWN:
            rectangle.move_ip(0, l)
            y += l
            if y >= Y + frame_side:
                fl_RIGHT_DOWN = False
            #print(f'X {X}  x {x}\t | Y {Y}  y {y} fl_RIGHT_DOWN {fl_RIGHT_DOWN}; вниз')

        elif x > X:
            rectangle.move_ip(-10, 0)
            x -= l
            #print(f'X {X}  x {x}\t | Y {Y}  y {y}; влево')

        elif y > Y:
            rectangle.move_ip(0, -10)
            y -= l
            #print(f'X {X}  x {x}\t | Y {Y}  y {y}; вверх')


    pygame.draw.rect(screen, square_color, rectangle, 0)

    pygame.display.flip()
    # pygame.display.update()  # Функции update() и flip() модуля display обновляют содержимое окна игры.
    # # Это значит, что каждому пикселю заново устанавливается цвет.
    # # Ограничение количества кадров в секунду, благодаря чему становится
    # проще просчитывать анимации и синхронизировать события
    clock.tick(FPS) # задержка в исполнении цикла (скорость движения)
























# def up_circle():
#     sc.fill(WHITE)  # "удаляем следы" - очищаем виджет, задаем цвет фона
#     pygame.draw.rect(sc, square_color, (x, y, l, l),0) # создаем новую фигуру (квадрат)
#     pygame.display.update()  # Функции update() и flip() модуля display обновляют содержимое окна игры.
#     # Это значит, что каждому пикселю заново устанавливается цвет.
#     # Ограничение количества кадров в секунду, благодаря чему становится
#     clock.tick(FPS) # проще просчитывать анимации и синхронизировать события
#
# while True:
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             sys.exit()
#
#         elif i.type == pygame.KEYDOWN and fl_start == False: # если еще не рисовали рамку
#             if i.key in [pygame.K_SPACE,    # нажата клавиша 'Пробел'
#                          pygame.K_RETURN,   # или 'Enter'
#                          pygame.K_KP_ENTER]:# или 'Enter'
#                 fl_start = True              # поднимем флаг начала отрисовки
#
#     # Моргаем, пока не начали рисовать
#     if fl_start == False:  #  - отрисовка еще не начата
#         if square_color[0] : # цвет красный (255, ..., ...)
#             square_color = color1 # перекрасим в черный
#             clock.tick(FPS//5)
#         elif not square_color[0]: # цвет черный (0, ..., ...)
#             square_color = color2  # перекрасим в красный
#             clock.tick(FPS//5)
#     else:
#         square_color = color1  # перекрасим в черный
#         x += l
#         pygame.draw.rect(sc, square_color, (x, y, l, l), 0)  # создаем новую фигуру (квадрат)
#
#     up_circle()  # Функция up_circle() обновляет содержимое окна игры + обеспечивает .

