# Задание № 02-1(PyGame)
# Написать программу, которая будет писать в консоль названия нажатых клавиш.
# Реализовать поддержку enter, space, w, a, s, d, esc.
# Названия кнопок внутри библиотеки доступны в официальной документации: https://www.pygame.org/docs/ref/event.html

import pygame # импортируем модуль pygame в наш файл с исходным кодом
from pygame.constants import*
import sys  # -/- модуля sys

# Создадим виджет работы программы
pygame.init()  # функция init() для подготовки модулей pygame к работе
screen = pygame.display.set_mode((20, 20))
rect = pygame.Rect(0, 0, 0, 0)
# color = (0, 0, 0)
print('Для выхода из программы нажать "Esc"\n'
      'Для теста нажмите любую из (enter, space, w, a, s, d, esc) клавиш:')
s = 'Нажата клавиша '

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            pressed_keys = pygame.key.get_pressed()
            if  pressed_keys[K_ESCAPE]:
                print(s, 'Esc\nПрограмма завершила свою работу')
                pygame.quit()
                sys.exit()
            elif pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER]: print(s, 'Enter')
            elif pressed_keys[K_SPACE]: print(s, 'Пробела')
            elif pressed_keys[K_w]: print(s, 'w')
            elif pressed_keys[K_a]: print(s, 'a')
            elif pressed_keys[K_s]: print(s, 's')
            elif pressed_keys[K_d]: print(s, 'd')
            else: print(s, pygame.key.name([pressed_keys]))












#
#
# screen = pygame.display.set_mode((500, 500))  # создаем графическое окно (основной виджет)
# screen.fill((255, 255, 255))  # фон основного окна виджета
#
# # ТЕКСТ! Для вставки текста
# # От классов pygame.font.Font и pygame.font.SysFont создаются объекты-шрифты.
# f = pygame.font.SysFont('arial', 28) # Второй класс берет системные шрифты, поэтому конструктору достаточно передать имя шрифта.
# # f = pygame.font.Font(None, 36) # Конструктору Font надо передавать имя файла шрифта.
# # В pygame есть шрифт по-умолчанию. Чтобы использовать его, вместо имени файла в конструктор надо передать объект None
#
# n = 1
# x = y = 0
# h = l = 50
# for i in range(10):  # создаем вертикальный ряд квадратов (№ столбца)
#     for ii in range(10):  # создаем горизонтальный ряд квадратов (№ строки)
#         # при толщине линии квадрата "0" окрашивается весь квадрат
#         # colored = random.randint(0,1)# генерируем толщину  линии квадрата
#         colored = random.choices([0, 1], weights=[0.3, 0.7])  # генерируем толщину  линии квадрата по вероятностям
#         if not colored[0]: # условие заливки всего квадрата, сгенерируем ему цвет
#             square_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#         else:# если выпола толщина 1px
#             square_color = (0, 0, 0) # щкрасим ее в черный цвет
#
#         pygame.draw.rect(screen, square_color, (x, y, h, l),colored[0]) # рисуем квадрат
#         text = f.render(str(n), True, (0, 0, 0)) # формируем объект текст
#         screen.blit(text, (x+5, y+7)) # вставляем текст
#         n += 1  # следующий номер квадрата
#         x += 50  # сместим кординату x для следующего квадрата горизонтального ряда
#     y += 50 # сместим кординату y для следующего квадрата столбца
#     x = 0  # в новый вертикальный ряд квадратов начнем с координаты x = 0
#
# # цикл программы, в котором, среди всех событий, происходящих в нашем приложении,
# # перехватываем событие закрытия основного графического окна пользователем
# while True:  # После того как ожидаемое событие наступило
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()  # завершаем работу с библиотекой pygame
#             sys.exit()  # завершаем работу нашей программы вызовом функции exit() из модуля sys.
#     pygame.display.flip()
