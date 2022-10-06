# Задание № 01-3(PyGame)
# Разработайте программу, которая разбивает основное игровое окно на клетки заданного размера.

import pygame  # импортируем модуль pygame в наш файл с исходным кодом
import sys  # -/- модуля sys

pygame.init()  # функция init() для подготовки модулей pygame к работе

screen = pygame.display.set_mode((500, 500))  # создаем графическое окно (основной виджет)
screen.fill((255, 255, 255))  # фон основного окна виджета

x = y = 0
h = l = 50
for i in range(10):  # создаем вертикальный ряд квадратов
    for ii in range(10):  # создаем горизонтальный ряд квадратов
        pygame.draw.rect(screen, (0, 0, 0), (x, y, h, l), 1) # рисуем квадрат
        x += 50  # сместим кординату x для следующего квадрата горизонтального ряда
    y += 50 # сместим кординату y для следующего квадрата столбца
    x = 0  # в новый вертикальный ряд квадратов начнем с координаты x = 0

# цикл программы, в котором, среди всех событий, происходящих в нашем приложении,
# перехватываем событие закрытия основного графического окна пользователем
while True:  # После того как ожидаемое событие наступило
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # завершаем работу с библиотекой pygame
            sys.exit()  # завершаем работу нашей программы вызовом функции exit() из модуля sys.
    pygame.display.flip()
