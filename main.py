# Ethan Lawrence
# May 16 2025
# Sprites

import random
import pygame
pygame.init()

class Game:
    '''Game Logic'''
    def __init__(self):
        self.shapes = pygame.sprite.Group()
        self.running = True
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('sprite test')
        self.clock = pygame.time.Clock()
        self.count = 0
        self.main()
    def main(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
    def handle_events(self):
        '''Checks if user quits game'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def draw(self):
        self.screen.fill((0,0,255))
        self.shapes.draw(self.screen)
        pygame.display.flip()
    def update(self):
        self.shapes.update()
        self.count += 1
        if self.count == 60:
            self.count = 0
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_SPACE]:
            self.shapes.add(some_shape((300,300), (random.randrange(0,255),random.randrange(0,255), random.randrange(0,255)), (10,10), (100, 50), random.randint(0,1)))

class some_shape(pygame.sprite.Sprite):
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

rungame = Game()
