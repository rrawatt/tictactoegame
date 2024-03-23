import pygame
from pygame.locals import *

grey = (33, 33, 33)
slate = (192, 194, 201)
cloud = (123, 123, 123)

class Box:
    def __init__(self, i, j, n):
        self.i = i
        self.j = j
        self.n = n
        self.rect = pygame.Rect(240 * i, 240 * j, 240, 240)
        self.clicked = False  # Track whether the box is clicked

    def draw_box(self,WIN):
        color = grey
        pygame.draw.rect(WIN, color, self.rect)
        pygame.draw.rect(WIN, cloud, self.rect, 5)

        if self.clicked and self.n == 0:
            pygame.draw.circle(WIN, cloud, (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2), 100, 10)
        elif self.clicked and self.n == 1:
            x, y = (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)
            half_size = 175 // 2
            pygame.draw.line(WIN, cloud, (x - half_size, y - half_size), (x + half_size, y + half_size), 15)
            pygame.draw.line(WIN, cloud, (x + half_size, y - half_size), (x - half_size, y + half_size), 15)

    def is_hover(self, pos):
        return self.rect.collidepoint(pos)

    def is_clicked(self, pos, click, p):
        clicked = self.rect.collidepoint(pos) and click
        if clicked and not self.clicked:
            self.clicked = True  # Set the clicked state
            self.n = 1 if p % 2 == 1 else 0  # Set the value based on p
            return True
        return False