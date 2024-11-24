import pygame
import sys

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
            self.states[self.gameStateManager.getState()].run()
            pygame.display.update()
            self.clock.tick(60)

class Level():
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('blue')

class Start():
    def __init__(self, display, gameStateManager):
        self.display = display
        self.gameStateManager = gameStateManager
    def run(self):
        self.display.fill('red')

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
