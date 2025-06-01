import pygame

class TextShowRandomItem:
    def __init__(self, text_content,screenWidth,screenHeight, color=(0, 0, 0), font_name=None):
       
        self.text_content = text_content
        self.color = color
        self.font_name = font_name
        self.fontSize = 32
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
     
        self.font = pygame.font.Font(self.font_name, self.fontSize)


        self.display_start_time = None
        self.display_duration = 1000
        self.active = False 

        self._update_surface()

    def show(self):
        self.active = True
        self.display_start_time = pygame.time.get_ticks()

    def kill(self):
        self.active = False
        self.display_start_time = None

    def _update_surface(self):
     
        self.surface = self.font.render(self.text_content, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.screenWidth // 2, self.screenHeight // 2 - 100)
    
    def draw(self, surface):
       
        if self.active:
            current_time = pygame.time.get_ticks()
            if self.display_start_time is not None and (current_time - self.display_start_time < self.display_duration):
                surface.blit(self.surface, self.rect)
            else:

                self.kill()