import pygame

class GameObj2D(pygame.sprite.Sprite):
    def __init__(self, on, x, y, width, height, image, in_obj):
        self.on = on  # on - номер объекта
        self.x = x  # х координата
        self.y = y  # у координата
        self.height = height  # высота
        self.width = width  # длина
        self.image = pygame.image.load(image)
        self.in_obj = in_obj  # дочерние объекты
    def place(self, window):
        window.blit(self.image, (self.x, self.y))
class AnimGameObj2d(GameObj2D):
    def __init__(self, images, time, FPS):
        self.images = images
        self.time = time
        self.FPS = FPS
        self.oof = FPS * self.time
        
