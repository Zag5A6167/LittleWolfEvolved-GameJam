import pygame
import os
spriteWidth = 64    
spriteHeight = 64

spriteScale = 6

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

    def animate_idle(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_speed * 1000:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = self.frames[self.current_frame]