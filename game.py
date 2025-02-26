import pygame
import input
from player import Player
from sprite import sprites
from map import TileKind, Map

pygame.init()

# Setup
pygame.display.set_caption("Arcanum Valley")
screen = pygame.display.set_mode((800,600))
clear_color = (30, 150, 50)
running = True
player = Player("images/idle.png",150,50)
tile_kinds = [
	TileKind("dirt", "images/dirt.png", False),
	TileKind("grass", "images/grass.png", False),
	TileKind("water", "images/water.png", False),
	TileKind("wood", "images/wood.png", False),
]

map = Map("maps/start.map", tile_kinds, 32)

# Game Loop:

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

	# Update Code
	player.update()

	# Draw Code
	screen.fill(clear_color)
	map.draw(screen)
	for s in sprites:
		s.draw(screen)
	pygame.display.flip()
	pygame.time.delay(10)

pygame.quit()