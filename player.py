import pygame
from sprite import Sprite
from input import is_key_pressed
from camera import set_camera_center


class Player(Sprite):
    def __init__(self, image, x, y):
        super().__init__(image, x, y)
        self.movement_speed = 1
        set_camera_center(x, y)

    def update(self):
        if is_key_pressed(pygame.K_w) and not self.colliding_forward():
            self.move_forward()
        if is_key_pressed(pygame.K_d) and not self.colliding_right():
            self.move_right()
        if is_key_pressed(pygame.K_s) and not self.colliding_backward():
            self.move_back()
        if is_key_pressed(pygame.K_a) and not self.colliding_left():
            self.move_left()
        set_camera_center(self.x, self.y)

    def colliding_forward(self):
        return False

    def colliding_right(self):
        return False

    def colliding_backward(self):
        return False

    def colliding_left(self):
        return False

    def move_forward(self):
        self.y -= self.movement_speed

    def move_right(self):
        self.x += self.movement_speed

    def move_back(self):
        self.y += self.movement_speed

    def move_left(self):
        self.x -= self.movement_speed
