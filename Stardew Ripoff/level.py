import pygame
from settings import *
from player import Player

class Level:
    def __init__(self):
        
        # gets a reference adress to the currently set display surface
        self.display_surface = pygame.display.get_surface()
        
        
        #class "group" is a part of pygame's sprite support. it is a class that manages a *list* of spries no cap.
        self.all_sprites = pygame.sprite.Group()
        
    def setup(self):
        self.player = Player((640, 360), self.all_sprites)
    
    
    def run(self, dt):
        #print("Ran GAM")
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface) # a draw function from the grp class
        self.all_sprites.update() # another function from the grp class