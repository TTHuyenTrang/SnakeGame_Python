import pygame

class Snake:
    def __init__(self, x, y):
        self.head = [x, y]              
        self.body = [[x, y]]            
        self.direction = "RIGHT"        

    def di_chuyen(self, rong, cao):
        if self.direction == "UP":
            self.head[1] -= 10
        elif self.direction == "DOWN":
            self.head[1] += 10
        elif self.direction == "LEFT":
            self.head[0] -= 10
        elif self.direction == "RIGHT":
            self.head[0] += 10

        self.head[0] %= rong
        self.head[1] %= cao

        self.body.insert(0, list(self.head))

    def cap_nhat_than(self, an_moi):
        if not an_moi:
            self.body.pop()

    def ve(self, cua_so):
        for pos in self.body:
            pygame.draw.rect(cua_so, (0,255 , 0), pygame.Rect(pos[0], pos[1], 10, 10))

    def kiem_tra_tu_can(self):
        return self.head in self.body[1:]
