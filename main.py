# Ethan Lawrence
# May 19 2025
# Tile Based Platformer

import random
import pygame
pygame.init()

# Global Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

TILE_SIZE = 100

# Images
class Game:
    '''Game Logic'''
    def __init__(self):
        self.solids = pygame.sprite.Group()
        self.backround_objects = pygame.sprite.LayeredUpdates()

        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('sprite test')
        self.clock = pygame.time.Clock()
        self.count = 0
        self.backround_objects.add(Backround_object((SCREEN_WIDTH/10, SCREEN_HEIGHT/10), 'sun.png', (255, 255, 255), layer=1))
        self.new_stage()
        self.main()
    def main(self):
        '''main game loop'''
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()
            self.draw_grid()
            pygame.display.flip()
    def handle_events(self):
        '''Checks if user quits game'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                self.running = False
    def new_stage(self):
        '''builds next stage'''
        self.backround_objects.remove_sprites_of_layer(10)
        self.backround_objects.add(Backround_object((random.randint(0, SCREEN_WIDTH), random.randint(0, 200)), 'cloud.png', (0, 0, 0)))
        self.backround_objects.add(Backround_object((random.randint(0, SCREEN_WIDTH), random.randint(0, 200)), 'cloud.png', (0, 0, 0)))
        self.backround_objects.add(Backround_object((random.randint(0, SCREEN_WIDTH), random.randint(0, 200)), 'cloud.png', (0, 0, 0)))

        this_stage = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        y = -1
        for row in this_stage:
            y += 1
            x = -1
            for tile in row:
                x += 1
                if tile == 1:
                    print(row, tile)
                    self.solids.add(Backround_object((x*TILE_SIZE, y*TILE_SIZE), 'ground.png', (255, 255, 255)))
    def draw(self):
        '''draws game objects'''
        self.screen.fill((0,0,255))
        self.solids.draw(self.screen)
        self.backround_objects.draw(self.screen)
    def update(self):
        '''Finds player inputs and game outputs'''
        self.count += 1
        if self.count == 60:
            self.count = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                self.new_stage()
    def draw_grid(self):
        for line in range(1, int(SCREEN_HEIGHT/TILE_SIZE)):
            pygame.draw.line(self.screen, (255, 255, 255), (0, line*TILE_SIZE), (SCREEN_WIDTH, line*TILE_SIZE))
        for line in range(1, int(SCREEN_WIDTH/TILE_SIZE)):
            pygame.draw.line(self.screen, (255, 255, 255), (line*TILE_SIZE, 0), (line*TILE_SIZE, SCREEN_HEIGHT))
class Backround_object(pygame.sprite.Sprite):
    def __init__(self, pos, image, color_key, layer=10):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self._layer = layer
        self.image = pygame.image.load(image)
        self.image.set_colorkey(color_key)
        self.rect = (self.x, self.y)
class Solid_object(pygame.sprite.Sprite):
    def __init__(self, pos, image, color_key, layer=10):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self._layer = layer
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        # self.image.set_colorkey(color_key)
        self.rect = (self.x, self.y)

rungame = Game()
