import pygame
from settings import *
from support import *
from timer import *

class Player(pygame.sprite.Sprite):
    
    
    def __init__(self, pos, group):
        super().__init__(group)
        
        #general setup
        self.image = pygame.Surface((32, 64))
        self.image.fill("green")
        self.rect = self.image.get_rect(center = pos)
        self.import_assets()
        self.status = 'down_idle'
        self.frame_index = 0
        self.z = LAYERS["main"]
        
        #movement attributes------
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        
        #timers
        
        self.timers = {
            "tool use": Timer(350, self.use_tool),
            "tool switch": Timer(200),
            "seed use": Timer(350, self.use_seed),
            "seed switch": Timer(200)
            }
        
        #tools
        self.tools = ['hoe', 'axe', 'water',]
        self.tool_index = 0 #default value is hoe no cap
        self.selected_tool = self.tools[self.tool_index]
        
        #seeds
        self.seeds = ["corn", "tomato", "diamondswod", "pumppie", "xmastree", "spongegar", "bingchillin", "sausage", "nerfgun", "21savage"]
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]
    
  #end of constructer----------------------------------  
    
    def use_tool(self):
        pass
        # print(self.selected_tool)
    
    def use_seed(self):
        pass
        # print(self.selected_seed) 
     
     
    def import_assets(self):
        self.animations = {'up':[], 'down':[], 'left':[], 'right':[],
                           'right_idle':[], 'left_idle':[], 'up_idle':[], 'down_idle':[],
                           'right_hoe':[], 'left_hoe':[], 'up_hoe':[], 'down_hoe':[],
                           'right_axe':[], 'left_axe':[], 'up_axe':[], 'down_axe':[],
                           'right_water':[], 'left_water':[], 'up_water':[], 'down_water':[]}
        
        
        for animation in self.animations.keys():
            full_path = '../graphics/character/' + animation
            self.animations[animation]=import_folder(full_path)
        # print(self.animations)
    
    
        
    
    def animate(self, dt): #animation method
        self.frame_index += int(4*dt) #increase frame number
        #print(self.status,self.animations[self.status])
        if self.frame_index >= len(self.animations[self.status]): #check if we've reached the end of the frame list
            self.frame_index = 0 # reset the frame index if we've reached the end
        self.image = self.animations[self.status][int(self.frame_index)]
        
        
    
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
                self.timers['tool use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
        #change tool
            if keys[pygame.K_q] and not self.timers["tool switch"].active:
                self.timers["tool switch"].activate()
                self.tool_index += 1
                self.tool_index = self.tool_index if self.tool_index < len(self.tools) else 0
                self.selected_tool = self.tools[self.tool_index]
                #if tool index > length of tools, then set tool index = 0
        
        # seed use
            if keys[pygame.K_LCTRL]:
                self.timers['seed use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
                #print("use seed")
        
        
        #change seed
            if keys[pygame.K_e] and not self.timers["seed switch"].active:
                self.timers["seed switch"].activate()
                self.seed_index += 1
                #if seed index > length of seed, then sed seed index = 0
                self.seed_index = self.seed_index if self.seed_index < len(self.seeds) else 0
                self.selected_seed = self.seeds[self.seed_index]
                #print(self.selected_seed)
        
        
        
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
       
       #horizontal movement     
        #print(self.direction)
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
       
       #vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y
    
    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)            
                
    def get_status(self):
        #check if the player is not moving:
        if self.direction.magnitude() == 0:
            #add_idle to the status
            self.status = self.status.split("_")[0] + "_idle"
        #tool use
            if self.timers['tool use'].active:
                # print("tool is being used")
                self.status = self.status.split("_")[0] + "_" + self.selected_tool
                self.frame_index = 0
    
    
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
    
    

    
    
            
            
            
            
