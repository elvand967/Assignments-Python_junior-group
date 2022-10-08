# Задание № 02-3(PyGame)
# источник https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/19-animations.html
# Написать программу, в которой по нажатию клавиш будет двигаться квадрат размером 20х20 пикселей.
# Учесть, что квадрат не должен выходить за границы экрана.

import sys
import pygame
import random

pygame.init()

# словарь цветов (color_dictionary)
cd = {'red':(255,0,0), 'orange':(255,128,0),
                    'yellow':(255,255,0), 'green':(0,128,0),
                    'blue':(0,0,255),'violet':(238,130,238),
                    'black':(0,0,0),'white':(255,255,255),
                    'gray':(128,128,128)}

W = 500  # ширина экрана
H = 500  # высота экрана

# определяем середину экрана виджета
X = x = W // 2 # X - исходные  x - фактические
Y = y = H // 2
shape_color = cd['blue'] # цвет фигуры
l = 20     # ширина прямоугольника (квадрата)
h = 20     # высота прямоугольника (квадрата)

# функия генератор цветов, котороя в качестве аргументов принимает...
def f_color_generator(color_dictionary, exclude_color = None ): # словарь цветов и цвет который нужно исключить
    # словарь цветов (color_dictionary)
    # color_dictionary = {'red': (255, 0, 0), 'orange': (255, 128, 0),...}
    list_color = list(color_dictionary) # преобразуем наш словарь цветов в список ключей типа: ['red','orange',...]
    if exclude_color is not None:   # если указан цвет для искючения, в виде 'white'...
        list_color.remove(exclude_color)  # ... удалим его из списка
    shape_color = cd[random.choice(list_color)] # генерируем случайный цвет в виде кортежа, пример: (0, 128, 0)
    return shape_color # кортеж (..., ..., ...)



screen = pygame.display.set_mode((W, H))
rect_border = pygame.Rect(0, 0, W, H) # Создадим границу поля монитора
rect = pygame.Rect(x, y, l, h)        # Создадим наш квадрат
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT:
                rect.move_ip(-l, 0)
            elif event.key == pygame.K_RIGHT:
                rect.move_ip(l, 0)
            elif event.key == pygame.K_UP:
                rect.move_ip(0, -h)
            elif event.key == pygame.K_DOWN:
                rect.move_ip(0, h)

    screen.fill(cd['white'])
    pygame.draw.rect(screen, cd['gray'], rect_border, 1)

    # если наш квадрат вышел за пределя границы (фигуры - 'rect_border')
    if not pygame.Rect.contains(rect_border, rect):
        shape_color = f_color_generator(cd, 'white') # перекрасим наш наш квадрат
        rect = pygame.Rect(X, Y, l, h) # вернем его в сиридину

    pygame.draw.rect(screen, shape_color, rect, 0) # отобразим наш квадрат

    pygame.display.flip()