import pygame

class FrameRateDisplay():
    def __init__(self, screen, update_interval, x_position, y_position):
        self.frames = 0
        self.frame_rate = 0
        self.time = update_interval
        self.update_interval = update_interval
        self.screen = screen
        self.font = pygame.font.SysFont("Calibri", 25, False, False)
        self.xpos = x_position
        self.ypos = y_position
        
    def update(self):
        if (self.time > pygame.time.get_ticks()):
            self.frames += 1
        else:
            self.frame_rate = int(self.frames / (float(self.update_interval) / 1000))
            self.frames = 1
            self.time += self.update_interval
        
        text = self.font.render(str(self.frame_rate), False, (0,0,0))
        self.screen.blit(text, (self.xpos, self.ypos))