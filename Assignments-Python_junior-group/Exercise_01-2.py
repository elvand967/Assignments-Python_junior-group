# Задание № 01-2
# Используя функции для работы с графикой библиотеки pygame,
# нарисуйте белый флаг с олимпийскими кольцами.

import pygame #  импортируем модуль pygame в наш файл с исходным кодом
import sys    # -/- модуля sys

pygame.init() # функция init() для подготовки модулей pygame к работе

screen = pygame.display.set_mode((300, 300)) # создаем графическое окно (основной виджет)
# Для создания объекта этого типа нам необходимо ...
r = pygame.Rect(60, 100, 160, 80)# ... указать координаты левого верхнего угла квадрата и длины его сторон
pygame.draw.rect(screen, (255, 255, 255), r, 0)# ... указать координаты левого верхнего угла квадрата и длины его сторон
col_circle = ((255, 0, 0),(0, 255, 0),(0, 0, 255),(0, 255, 255),(255, 0, 255))
n = 125
h = 110
for i in range(5):
    if i==3:
        n+=28
        h-=75
    pygame.draw.circle(screen, col_circle[i],(h+(i*30), n),20,3)

# цикл программы, в котором, среди всех событий, происходящих в нашем приложении,
# перехватываем событие закрытия основного графического окна пользователем
while True: # После того как ожидаемое событие наступило
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # завершаем работу с библиотекой pygame
            sys.exit()    # завершаем работу нашей программы вызовом функции exit() из модуля sys.
    pygame.display.flip()