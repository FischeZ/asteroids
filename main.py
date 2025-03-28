import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    pl_loc_x = SCREEN_WIDTH / 2
    pl_loc_y = SCREEN_HEIGHT / 2
    Player.containers = (updatable, drawable)
    player = Player(pl_loc_x, pl_loc_y)

    dt = 0
    
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        pygame.Surface.fill(screen, (0, 0, 0))
        updatable.update(dt)
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        time_passed = clock.tick(60)
        dt = time_passed / 1000

if __name__ == "__main__":
    main()