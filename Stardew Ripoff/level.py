import pygame
from settings import *
from player import Player 
from overlay import Overlay
from sprites import Generic

class Level:
    def __init__(self):
        
        # gets a reference adress to the currently set display surface
        self.display_surface = pygame.display.get_surface()
        
        #class "group" is a part of pygame's sprite support. it is a class that manages a *list* of spries no cap.
        
        self.all_sprites = CameraGroup()
        #self.all_sprites = pygame.sprite.Group()
        
        self.setup() #call the setup function
        self.overlay = Overlay(self.player)
        
    def setup(self):
        Generic(
            pos = (0,0),
            surf = pygame.image.load("../graphics/world/ground.png").convert_alpha(),
            groups = self.all_sprites,
            z = LAYERS["ground"])
        
        self.player = Player((640, 360), self.all_sprites) #this gets handed a position
    
    
    def run(self, dt):
        #print("RAN GAM")
        
        self.display_surface.fill('black')
        #self.all_sprites.draw(self.display_surface)
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.display()
        
        
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface() #lets you draw on the surfaces
        self.offset = pygame.math.Vector2()
        
    def custom_draw(self, player):
        #shift all sprites relative to the player!
        #this logic snesures that the player is always at the center of the screen
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
            
             
