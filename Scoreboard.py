import pygame

class Scoreboard():
    def __init__(self,screen):
        self.score = 0
        self.font=pygame.font.Font(None, 36)
        try:
            file = open("highscore.txt", 'x')
            file.write("0")
            file.close()
            file = open("highscore.txt", 'r')
        except FileExistsError:
            file = open("highscore.txt", 'r')
        finally:
            self.highScore = int(file.read())
            file.close()
        self.screen = screen
    def displayScore(self):
        score_surface = self.font.render(f'Score: {self.score} Highscore: {self.highScore}', True, (255, 255, 255))
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 10)
        self.screen.blit(score_surface, score_rect)
    def increaseScore(self):
        self.score += 1
        self.displayScore()

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
            file=open("highscore.txt",'w')
            file.write(str(self.highScore))
            file.close()
        self.score = 0
        self.displayScore()
