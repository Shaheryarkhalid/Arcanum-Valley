import pygame
from CONSTANTS import TILE_SIZE
import input
from player import Player
from sprite import sprites
from map import TileKind, Map
from camera import create_screen


# Setup
pygame.init()

# Constants

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER = Player("images/idle.png", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
CLOCK = pygame.time.Clock()
CLEAR_COLOR = (30, 150, 50)
TILE_KINDS = [
    TileKind("dirt", "images/dirt.png", True),
    TileKind("grass", "images/grass.png", True),
    TileKind("water", "images/water.png", False),
    TileKind("wood", "images/wood.png", True),
    TileKind("tree", "images/tree.png", False),
]
MAP = Map("maps/start.map", TILE_KINDS, TILE_SIZE)
SCREEN = create_screen(SCREEN_WIDTH, SCREEN_HEIGHT, "Arcanum Valley")

running = True
dt = 0


# Game Loop:


def main():
    global running
    global dt
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
        PLAYER.update()

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
