import pygame
import input
from player import Player
from sprite import sprites
from map import TileKind, Map

# Setup
pygame.init()
pygame.display.set_caption("Arcanum Valley")
# Constants

SCREEN = pygame.display.set_mode((800, 600))
CLOCK = pygame.time.Clock()
CLEAR_COLOR = (30, 150, 50)
TILE_KINDS = [
    TileKind("dirt", "images/dirt.png", False),
    TileKind("grass", "images/grass.png", False),
    TileKind("water", "images/water.png", False),
    TileKind("wood", "images/wood.png", False),
]
MAP = Map("maps/start.map", TILE_KINDS, 32)

running = True
dt = 0


# Game Loop:


def main():
    global running
    global dt

    updateables = pygame.sprite.Group()

    Player.containers = (updateables,)

    player = Player("images/idle.png", 150, 50)
    while running:
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                running = False
            # Handle Pressed Keys
            elif event.type == pygame.KEYDOWN:
                input.keys_down.add(event.key)
            elif event.type == pygame.KEYUP:
                input.keys_down.remove(event.key)

        # Update Code*
        updateables.update()
        # player.update()

        # Draw Code
        SCREEN.fill(CLEAR_COLOR)
        MAP.draw(SCREEN)
        for s in sprites:
            s.draw(SCREEN)
        pygame.display.flip()
        dt = CLOCK.tick(60)
        # pygame.time.delay(10)

    pygame.quit()


if __name__ == "__main__":
    main()
