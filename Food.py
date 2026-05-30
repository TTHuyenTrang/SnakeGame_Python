import pygame, random

class Food:
    def __init__(self, rong, cao):
        self.rong = rong
        self.cao = cao
        self.vi_tri = [random.randrange(1, rong//10)*10,
                       random.randrange(1, cao//10)*10]

    def tao_moi(self):
        self.vi_tri = [random.randrange(1, self.rong//10)*10,
                       random.randrange(1, self.cao//10)*10]

    def ve(self, cua_so):
        pygame.draw.rect(cua_so, (255, 0, 0), pygame.Rect(self.vi_tri[0], self.vi_tri[1], 10, 10))
