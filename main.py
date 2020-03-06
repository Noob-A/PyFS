# импорты
import pygame
import time
import sys
from pygame.locals import *
# from classes import *

pygame.init()
# загрузка текстур закрылок
flapsFrame = []  # пустой массив
for framenum in range(4):  # в каждый элемент пихаем наш путь
    flapsFrame.append(
        # Итог: мы прописали локации каждого кадра в массив
        pygame.image.load(f'./textures/Panel/temp/{framenum+1}_frame.png'))

# иницилизация
pygame.init()
# константы
FPS = 60
disp_w = 500
disp_h = 500
# переменные

# объекты
window = pygame.display.set_mode((disp_w, disp_h))
pygame.display.set_caption('test caption')
clock = pygame.time.Clock()

# главный цикл
def main():
    # вечный цикл
    while True:

        # обработка событий
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    for lol in range(4):
                        window.blit(flapsFrame[lol], (0, 0))
                        time.sleep(0.1)
                        pygame.display.update()
        if event.type == pygame.QUIT:
            return
        pygame.display.update()  # обновление экрана
        clock.tick(FPS)  # задержка
main()
