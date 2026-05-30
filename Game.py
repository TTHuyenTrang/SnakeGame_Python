import pygame, sys
from Snake import Snake
from Food import Food

class Game:
    def __init__(self, rong=600, cao=400):
        self.rong, self.cao = rong, cao
        self.cua_so = pygame.display.set_mode((rong, cao))
        pygame.display.set_caption("Snake Game")
        self.dong_ho = pygame.time.Clock()
        self.snake = Snake(rong//2, cao//2)
        self.food = Food(rong, cao)
        self.diem = 0

    def hien_thi_diem(self):
        font = pygame.font.Font(None, 20)
        score = font.render(f"Point: {self.diem}", True, (255, 255, 255))
        self.cua_so.blit(score, (10, 10))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.snake.direction != "DOWN":
                        self.snake.direction = "UP"
                    elif event.key == pygame.K_DOWN and self.snake.direction != "UP":
                        self.snake.direction = "DOWN"
                    elif event.key == pygame.K_LEFT and self.snake.direction != "RIGHT":
                        self.snake.direction = "LEFT"
                    elif event.key == pygame.K_RIGHT and self.snake.direction != "LEFT":
                        self.snake.direction = "RIGHT"

            self.snake.di_chuyen(self.rong, self.cao)
            
            an_moi = False
            if self.snake.head == self.food.vi_tri:
                self.diem += 1
                an_moi = True
                self.food.tao_moi()

            self.snake.cap_nhat_than(an_moi)

            if self.snake.kiem_tra_tu_can():
                font = pygame.font.Font(None, 50)
                game_over_text = font.render("GAME OVER", True, (255, 0, 0))
                rect = game_over_text.get_rect(center=(self.rong//2, self.cao//2))
                self.cua_so.blit(game_over_text, rect)
                pygame.display.update()

                waiting = True
                while waiting:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit(); sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                            waiting = False   
                return

            self.cua_so.fill((0, 0, 0))
            self.snake.ve(self.cua_so)
            self.food.ve(self.cua_so)
            self.hien_thi_diem()
            pygame.display.update()
            self.dong_ho.tick(10)


class Menu:
    def __init__(self, rong=600, cao=400):
        self.rong, self.cao = rong, cao
        self.cua_so = pygame.display.set_mode((rong, cao))
        pygame.display.set_caption("Snake Game")
        self.font = pygame.font.Font(None, 40)
        self.clock = pygame.time.Clock()

    def ve_text(self, text, x, y, color=(255,255,255)):
        render = self.font.render(text, True, color)
        rect = render.get_rect(center=(x,y))
        self.cua_so.blit(render, rect)
        return rect

    def run(self):
        while True:
            self.cua_so.fill((0,0,0))  
            play_rect = self.ve_text("PLAY", self.rong//2, 150)
            option_rect = self.ve_text("OPTION", self.rong//2, 220)
            quit_rect = self.ve_text("QUIT", self.rong//2, 290)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if play_rect.collidepoint(event.pos):
                        game = Game(self.rong, self.cao)
                        game.run()
                    elif option_rect.collidepoint(event.pos):
                        self.show_option()
                    elif quit_rect.collidepoint(event.pos):
                        pygame.quit(); sys.exit()

            pygame.display.update()
            self.clock.tick(30)

    def show_option(self):
        running = True
        while running:
            self.cua_so.fill((0,128,0))
            self.ve_text("Hướng dẫn:", self.rong//2, 100)
            self.ve_text("↑ ↓ ← → : Di chuyển", self.rong//2, 160)
            self.ve_text("Ăn mồi để tăng điểm", self.rong//2, 200)
            self.ve_text("Tránh va vào thân rắn", self.rong//2, 240)
            self.ve_text("Nhấn ESC để quay lại", self.rong//2, 300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            pygame.display.update()
            self.clock.tick(30)
