# Ethan Lawrence
# May 19 2025
# Tile Based Platformer

import random
import pygame
pygame.init()

# Global Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

# Images
class Game:
    '''Game Logic'''
    def __init__(self):
        self.shapes = pygame.sprite.Group()
        self.backround_objects = pygame.sprite.Group()

        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('sprite test')
        self.clock = pygame.time.Clock()
        self.count = 0
        self.main()
    def main(self):
        self.backround_objects.add(Backround_object((150, 150), 'cloud.png', (17, 193, 242)))
        self.backround_objects.add(Backround_object((100, 150), 'cloud.png', (17, 193, 242)))
        self.backround_objects.add(Backround_object((100, 100), 'cloud.png', (17, 193, 242)))
        self.backround_objects.add(Backround_object((100, 100), 'sun.png', (255, 255, 255)))
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
    def handle_events(self):
        '''Checks if user quits game'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                self.running = False
    def draw(self):
        self.screen.fill((0,0,255))
        self.shapes.draw(self.screen)
        self.backround_objects.draw(self.screen)
        pygame.display.flip()
    def update(self):
        self.shapes.update()
        self.count += 1
        if self.count == 60:
            self.count = 0
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_SPACE]:
            self.shapes.add(Some_shape((300,300), (random.randrange(0,255),random.randrange(0,255), random.randrange(0,255)), (10,10), (100, 50), random.randint(0,1)))
class Some_shape(pygame.sprite.Sprite):
    def __init__(self, pos, color, speed, scale, shape):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.vel = speed
        self.rect = (self.x, self.y)
        self.scale = scale
        if shape == 0:
            self.image = pygame.Surface((scale[0], scale[1]))
            self.image.set_colorkey((0,0,0)) # removes the black border of the image
            self.image.fill(color)
        elif shape == 1:
            self.image = pygame.Surface((self.scale[0]*2, self.scale[1]*2))
            self.image.set_colorkey((0,0,0))
            pygame.draw.circle(self.image, self.color, (self.scale[0], self.scale[0]), self.scale[0])
    def update(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        self.rect = (self.x, self.y)
class Backround_object(pygame.sprite.Sprite):
    def __init__(self, pos, image, color_key):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.image = pygame.image.load(image)
        self.image.set_colorkey(color_key)
        self.rect = (self.x, self.y)

rungame = Game()
