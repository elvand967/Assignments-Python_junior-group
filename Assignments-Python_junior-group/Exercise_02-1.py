# Задание № 02-1(PyGame)
# источник https://python-course.readthedocs.io/projects/elementary/en/latest/lessons/19-animations.html
# Написать программу, которая будет писать в консоль названия нажатых клавиш.
# Реализовать поддержку enter, space, w, a, s, d, esc ++.
# Названия кнопок внутри библиотеки доступны в официальной документации: https://www.pygame.org/docs/ref/event.html

import pygame # импортируем модуль pygame в наш файл с исходным кодом
from pygame.constants import*
import sys  # -/- модуля sys

# Создадим виджет работы программы
screen = pygame.display.set_mode((270, 20))

print('Для выхода из программы нажать "Esc"\n'
      'Для теста нажмите любую из клавиш цифр или алфавита:')
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
            elif pressed_keys[K_RETURN] or pressed_keys[K_KP_ENTER]:
                print(s, 'Enter')
            elif pressed_keys[K_DELETE]:
                print(s, 'Delete')
            elif pressed_keys[K_RSHIFT] or pressed_keys[K_LSHIFT]:
                print(s, 'Shift')
            elif pressed_keys[K_RALT] or pressed_keys[K_LALT]:
                print(s, 'Alt')
            elif pressed_keys[K_RCTRL] or pressed_keys[K_LCTRL]:
                print(s, 'Control')
            elif pressed_keys[K_SPACE]:
                print(s, 'Пробела')
            else: print(s, event.unicode)
