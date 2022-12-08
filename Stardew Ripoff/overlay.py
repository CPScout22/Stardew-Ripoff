import pygame
from settings import *


class Overlay:
    def __init__(self, player):
        
        
        #general setup
        self.display_surface = pygame.display.get_surface() #a seperate surface for the overlay
        self.player = player
        
        
        #imports
        overlay_path = "../graphics/overlay/"
        self.tools_surf = {tool: pygame.image.load(f'{overlay_path}{tool}.png').convert_alpha() for tool in player.tools}
        self.seeds_surf = {seed: pygame.image.load(f'{overlay_path}{seed}.png').convert_alpha() for seed in player.seeds}
        print(self.tools_surf)
        print(self.seeds_surf)
        
    def display(self):
        #tools
        tool_surf = self.tools_surf[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(bottomright = OVERLAY_POSITIONS["tool"])
        self.display_surface.blit(tool_surf, tool_rect)
        
        #seeds
        seed_surf = self.seeds_surf[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(bottomleft = OVERLAY_POSITIONS["seed"])
        self.display_surface.blit(seed_surf, seed_rect)
        
        
    def run(self, dt):
        #print("run game")
        self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
        self.overlay.display()
                                    
                            
