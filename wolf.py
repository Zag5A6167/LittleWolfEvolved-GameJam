import pygame
import os
spriteWidth = 64    
spriteHeight = 64

spriteScale = 6

LIGHT_BLUE = (173, 216, 230) ### (Light Blue)

class Wolf(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__() 
        self.sprite_sheet = pygame.image.load(os.path.join("asset", "wolf", "idle", "wolf_idle.png")).convert_alpha()

       
        self.frames = []
        self.load_frames()

        self.current_frame = 0
        self.animation_speed = 0.05
        self.last_update = pygame.time.get_ticks()

        self.image = self.frames[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


        ## coin ## 
        self.coins = 0

        ### Status ###
        self.attack = 1
        self.defense = 1

        #####  Health bar & Font #####

        self.healthBar_width = 400
        self.healthBar_height = 40
        self.maxHealth = 100
        self.paddingTop = 20
        self.currentHealth = self.maxHealth
        
        self.healthBarFontColor = (255,255,255)
        self.healthBarFontSize = 30
        self.healthBarFont = pygame.font.Font(None,self.healthBarFontSize)

        ## Enery Bar #####
        self.energyBar_width = 400
        self.energyBar_height = 40
        self.maxEnergy = 100
        
        self.currentEnergy = 0
        
        self.energyBarFontColor = (255,255,255)
        self.energyBarFontSize = 30
        self.energyBarFont = pygame.font.Font(None,self.energyBarFontSize)
       
        self.last_energyBar_update = pygame.time.get_ticks()
        self.energyBar_update_delay = 100

        ### Status ATK DEF ... ###
    
        self.paddingX_status = 50
        self.paddingY_status = 10
        self.text_status = pygame.font.Font(None,32)
        self.text_status_atk_surface = self.text_status.render(f"ATK: {self.attack}",True,(255,255,255))
        self.text_status_atk_surface_rect = self.text_status_atk_surface.get_rect(center=(200,300)) 

        ## DEF###
        self.text_status_def_surface = self.text_status.render(f"DEF: {self.attack}",True,(255,255,255))
        self.text_status_def_surface_rect = self.text_status_def_surface.get_rect(center=(200,300)) 

        ########################

    def load_frames(self):
    
        scaledWidth = spriteWidth * spriteScale
        scaledHeight = spriteHeight * spriteScale
        
        for i in range(3): 
            frame = self.sprite_sheet.subsurface((i * spriteWidth, 0, spriteWidth, spriteHeight))
            scaledFrame =  pygame.transform.scale(frame, (scaledWidth, scaledHeight))
            self.frames.append(scaledFrame)

       
        for i in range(3): 
            frame = self.sprite_sheet.subsurface((i * spriteWidth, spriteHeight, spriteWidth, spriteHeight))
            scaledFrame =  pygame.transform.scale(frame, (scaledWidth, scaledHeight))
            self.frames.append(scaledFrame)

        
        frame = self.sprite_sheet.subsurface((0, 2 * spriteHeight, spriteWidth, spriteHeight))
        scaledFrame =  pygame.transform.scale(frame, (scaledWidth, scaledHeight))
        self.frames.append(scaledFrame)


    def update(self):
        self.animate_idle()
        self.updateStatus()
     
        

    def animate_idle(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]

    def addCoin(self,amount):
        self.coins += amount
        return self.coins

    def takeDamage(self,amount):
        self.currentHealth -= amount
        if self.currentHealth <= 0:
            self.currentHealth = 0
            print("Wolf is dead!")

        print(f"Wolf took {amount} damage. Current health: {self.currentHealth}")

    def draw_health_bar(self, screen, screen_width):
        bar_x = (screen_width // 2) - (self.healthBar_width // 2)
        bar_y = self.paddingTop

        fill_width = int((self.currentHealth / self.maxHealth) * self.healthBar_width)

        pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, self.healthBar_width, self.healthBar_height))
        pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, fill_width, self.healthBar_height))
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, self.healthBar_width, self.healthBar_height), 2)


        # --- Draw Health Text Center---
        health_text = self.healthBarFont.render(f"HP {self.currentHealth}/{self.maxHealth}", True, self.healthBarFontColor)
        text_x = bar_x + (self.healthBar_width // 2) - (health_text.get_width() // 2)
        text_y = bar_y + (self.healthBar_height // 2) - (health_text.get_height() // 2)
        screen.blit(health_text, (text_x, text_y))
   

    def draw_energy_bar(self, screen, screen_width):
        
        bar_x = (screen_width // 2) - (self.healthBar_width // 2)
        bar_y = self.paddingTop * 1.2  + self.healthBar_height

        fill_width = int((self.currentEnergy / self.maxEnergy) * self.energyBar_width)

        pygame.draw.rect(screen, (50, 50, 50), (bar_x, bar_y, self.energyBar_width, self.energyBar_height))

        ## prcess ###
        pygame.draw.rect(screen, (LIGHT_BLUE), (bar_x, bar_y, fill_width, self.energyBar_height))
        pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, self.energyBar_width, self.energyBar_height), 2)


        # --- Draw Energy Text Center---
        energy_text = self.energyBarFont.render(f"Energy {self.currentEnergy}/{self.maxEnergy}", True, self.energyBarFontColor)
        text_x = bar_x + (self.energyBar_width // 2) - (energy_text.get_width() // 2)
        text_y = bar_y + (self.energyBar_height // 2) - (energy_text.get_height() // 2)
        screen.blit(energy_text, (text_x, text_y))


    def updateEnergyBar(self):

        now = pygame.time.get_ticks()
        if now - self.last_energyBar_update > self.energyBar_update_delay:
            self.last_energyBar_update = now
            self.currentEnergy += 1
            if self.currentEnergy >= self.maxEnergy:
                self.currentEnergy = self.maxEnergy

    def updateStatus(self):
         self.text_status_surface = self.text_status.render(
            f"ATK: {self.attack}",
            True, 
            (255, 255, 255) 
            
        )
        
    def draw_status(self, screen):
    
        padding_top = 10
        ## ATK ###
        bar_x = (screen.get_width() // 2) - (self.healthBar_width // 2) 
        bar_y = self.paddingTop * 1.2  + self.healthBar_height + self.energyBar_height + padding_top

        bar_y_def = bar_y * 1.2 + padding_top
        screen.blit(self.text_status_atk_surface, (bar_x,bar_y))


        ## DEF ###
     

        screen.blit(self.text_status_def_surface, (bar_x,bar_y_def))



         


    