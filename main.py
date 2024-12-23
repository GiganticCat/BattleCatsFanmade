import pygame
import sys

dt = 0

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((680, 360))
        self.clock = pygame.time.Clock()
        self.gameStateManager = GameStateManager('start')
        self.start = Start(self.screen, self.gameStateManager)
        self.level = Level(self.screen, self.gameStateManager)
        
        self.states = {'start':self.start, 'level':self.level}
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill('white')
            self.states[self.gameStateManager.getState()].run()
            pygame.display.update()
            self.clock.tick(60)
class Button():
    def __init__(self, x, y, path, display, width, height, gameStateManager):
        self.currentState = 0
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.display = display
        self.image = pygame.image.load(path).convert_alpha()
        self.gameStateManager = gameStateManager
    def update(self, mouse_pos):
        self.display.blit(self.image, (self.x, self.y))
        if pygame.mouse.get_pressed()[0]:
            if self.x <= mouse_pos[0] <= self.x + self.width and self.y <= mouse_pos[1] <= self.y + self.height:
                self.gameStateManager.setState('level')
class Level():
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('blue')

class Start():
    def __init__(self, display, gameStateManager):
        self.display = display
        self.background = pygame.image.load('assets/background.png').convert()
        self.title1 = pygame.image.load('assets/title_1.png').convert_alpha()
        self.title2 = pygame.image.load('assets/title_2.png').convert_alpha()
        self.gameStateManager = gameStateManager
        self.startButton = Button(213, 200, 'assets/start_button.png', self.display, 254, 48, self.gameStateManager)
        self.title_T = 1
        self.states = {0: self.title1, 1: self.title2}
        self.last_switch_time = pygame.time.get_ticks()
        self.switch_interval = 250

    def run(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_switch_time >= self.switch_interval:
            self.title_T = (self.title_T + 1) % 2
            self.last_switch_time = current_time

        self.display.blit(self.background, (0, 0))
        self.display.blit(self.states[self.title_T], (240, 0))
        self.startButton.update(pygame.mouse.get_pos())

class GameStateManager():
    def __init__(self, currentState):
        self.currentState = currentState
    def getState(self):
        return self.currentState
    def setState(self, state):
        self.currentState = state

if __name__ == '__main__':
    game = Game()
    game.run()
