# Ethan Lawrence
# May 19 2025
# Tile Based Platformer

import random
import pygame
pygame.init()

# Global Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CLOCK = pygame.time.Clock()

TILE_SIZE = 50

STAGES = {
    1 : [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 2, 2, 2, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 2, 2, 2, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 9, 0, 0, 2, 2, 2, 0, 1, 0, 0, 0, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 9, 0, 0, 1],
        [1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 0, 0, 1]],

    2 : [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 1],
        [1, 2, 0, 2, 0, 0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 1],
        [1, 2, 9, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 1],
        [1, 2, 2, 2, 0, 2, 2, 2, 0, 2, 0, 2, 0, 0, 0, 1],
        [1, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 0, 1],
        [1, 2, 9, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 0, 2, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 0, 0, 0, 1],
        [1, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1]]
}
# Images
class Game:
    '''Game Logic'''
    def __init__(self):
        self.solids = pygame.sprite.LayeredUpdates()
        self.backround_objects = pygame.sprite.LayeredUpdates()
        self.players = pygame.sprite.Group()

        self.running = True
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('sprite test')
        self.count = 0
        self.stage = 1
        self.backround_objects.add(Backround_object((SCREEN_WIDTH/10, SCREEN_HEIGHT/10), 'sun.png', (255, 255, 255), layer=1))
        self.new_stage()
    def handle_events(self):
        '''Checks if user quits game'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                self.running = False
    def new_stage(self):
        '''builds next stage'''
        self.backround_objects.remove_sprites_of_layer(10)
        self.solids.remove_sprites_of_layer(10)
        self.backround_objects.add(Backround_object((random.randint(0, SCREEN_WIDTH), random.randint(0, 200)), 'cloud.png', (0, 0, 0)))
        self.backround_objects.add(Backround_object((random.randint(0, SCREEN_WIDTH), random.randint(0, 200)), 'cloud.png', (0, 0, 0)))
        self.backround_objects.add(Backround_object((random.randint(0, SCREEN_WIDTH), random.randint(0, 200)), 'cloud.png', (0, 0, 0)))

        this_stage = STAGES[self.stage]
        y = -1
        for row in this_stage:
            y += 1
            x = -1
            for tile in row:
                x += 1
                if tile == 1:
                    self.solids.add(Solid_object((x*TILE_SIZE, y*TILE_SIZE), 'stone.png', (255, 255, 255)))
                elif tile == 2:
                    self.solids.add(Solid_object((x*TILE_SIZE, y*TILE_SIZE), 'grass.png', (255, 255, 255)))
                elif tile == 9:
                    self.players.add(Player_character((x*TILE_SIZE, y*TILE_SIZE)))
    def draw(self):
        '''draws game objects'''
        self.screen.fill((0,0,255))
        self.backround_objects.draw(self.screen)
        self.solids.draw(self.screen)
        self.players.draw(self.screen)
    def update(self):
        '''Finds player inputs and game outputs'''
        self.players.update()

        self.count += 1
        if self.count == 60:
            self.count = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                self.new_stage()
    def draw_grid(self):
        for line in range(1, int(SCREEN_HEIGHT/TILE_SIZE)):
            pygame.draw.line(self.screen, (255, 255, 255), (0, line*TILE_SIZE), (SCREEN_WIDTH, line*TILE_SIZE))
        for line in range(1, int(SCREEN_WIDTH/TILE_SIZE)):
            pygame.draw.line(self.screen, (255, 255, 255), (line*TILE_SIZE, 0), (line*TILE_SIZE, SCREEN_HEIGHT))
# End Of Game Class

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
    def __init__(self, pos, image, color_key):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self._layer = 10
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.image.set_colorkey(color_key)
        self.rect = (self.x, self.y)

class Player_character(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.x = pos[0]
        self.y = pos[1]
        self.rect = (self.x, self.y)
        self.vel_y = 0
        self.jumped = False

        self.walking = False
        self.animation_delay = 0
        self.direction = 2
    
        # Image
        self.images = ['player_stand.png', 'player_step.png', 'player_big_step.png', 'player_step.png']
        self.current_image = 0
        self.image = pygame.image.load(self.images[self.current_image])
        self.image = pygame.transform.scale(self.image, (TILE_SIZE/5*4, TILE_SIZE/5*8))
    def update(self):
        # Get inputs
        keys = pygame.key.get_pressed()
        dx = 0
        dy = 0

        last_direction = self.direction
        if keys[pygame.K_a]:
            dx -= 5
            self.direction = 1
        if keys[pygame.K_d]:
            dx += 5
            self.direction = 2
        if keys[pygame.K_SPACE] and self.jumped == False:
            self.vel_y = -20
            self.jumped = True
        
        # Handle a+d input & walking textures
        if dx == 0:
            self.direction = last_direction # maintain direction
            self.walking = False
            if self.current_image != 0:
                self.walk_cycle()
        else:
            self.walking = True
            self.walk_cycle()

        # Gravity
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # Collider
        # Move X
        for sprite in get_world():
            sprite_rect = pygame.Rect(sprite.rect[0], sprite.rect[1],  TILE_SIZE, TILE_SIZE)
            
            if sprite_rect.colliderect(pygame.Rect(self.x+dx, self.y, TILE_SIZE/5*4, TILE_SIZE/5*8)):
                dx = 0
        self.x += dx
        # Move Y
        for sprite in get_world():
            sprite_rect = pygame.Rect(sprite.rect[0], sprite.rect[1],  TILE_SIZE, TILE_SIZE)
            
            player_rect = pygame.Rect(self.x, self.y+dy, TILE_SIZE/5*4, TILE_SIZE/5*8)
            if sprite_rect.colliderect(player_rect):
                if self.vel_y >= 0:
                    self.jumped = False
                dy = 0
                self.vel_y = 0
        self.y += dy

        self.rect = (self.x, self.y)

    def walk_cycle(self):
        self.animation_delay += 1
        if self.animation_delay == 5:
            self.animation_delay = 0
            self.current_image += 1
            if self.current_image == len(self.images):
                self.current_image = 0
            self.image = pygame.image.load(self.images[self.current_image])
            self.image = pygame.transform.scale(self.image, (TILE_SIZE/5*4, TILE_SIZE/5*8))
            if self.direction == 1:
                self.image = pygame.transform.flip(self.image, True, False)

def get_world():
    return rungame.solids
def get_player():
    return rungame.players

rungame = Game()
# main game loop
while rungame.running:
    CLOCK.tick(60)
    rungame.handle_events()
    rungame.update()
    rungame.draw()
    rungame.draw_grid()
    pygame.display.flip()