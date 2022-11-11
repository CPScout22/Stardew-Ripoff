import pygame
from settings import *
from support import *

class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, pos, group):
        super().__init__(group)
        
        self.import_assets()
        self.status = 'down_idle'
        self.fram_indx =0
        
    def animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]
        
        #general setup---------
        self.image = pygame.Surface((32,64))
        self.image.fill('green')
        self.rect = self.image.get_rect(center = pos)
        
        #movement attributes------
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
        
    def input(self):
        keys = pygame.key.get_pressed()
            if not self.timers['tool use'].active:
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = "up"
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = "down"
            
            else:
              self.direction.y = 0

            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = "left"
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = "right"
            else:
              self.direction.x = 0
        
            #print(self.direction)
            
        #tool use
            if keys[pygame.K_SPACE]:
                self.timers
    
    def get_status(self):
        #check if the player is not moving:
        if self.direction.magnitude() == 0:
            #add_idle to the status
            self.status = self.status.split("_")[0] + "_idle"
        #tool use
            if self.timers['tool use'].active:
                print("tool is being used")
    
    
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
       #horizontal movemen     
        print(self.direction)
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
       #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
    
    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)
        self.animate(dt)
        
    def import_assets(self):
        self.animations = {'up':[], 'down':[], 'left':[], 'right':[],
                           'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                           'right_hoe':[], 'left_hoe':[], 'up_hoe':[], 'down_hoe':[],
                           'right_axe':[], 'left_axe':[], 'up_axe':[], 'down_axe':[],
                           'right_water':[], 'left_water':[], 'up_water':[], 'down_water':[]}
        
        for animation in self.animations.leys():
            full_path = '../graphics/character/' + animation
            self.animations[animation]=import_folder(full_path)
        print(self.animations)
        
        #timers
        self.timers = {
            "tool use": Timer(350, self.use_tool)
            }
    
        #tools
        self.selected_tool = "axe"
    
    def use_tool(self):
        print(self.selected_tool)
    
    
    
    
    
    
    
    
    
    
    
    
    
    