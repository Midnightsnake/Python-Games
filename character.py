import pygame

class Character:
    def __init__(self, position):
        self.position = position

    def setposition(self, x, y):
        self.position = (x, y)

    def move(self, dx, dy):
        x = self.position[0]
        y = self.position[1]
        self.position = (x + dx, y + dy)