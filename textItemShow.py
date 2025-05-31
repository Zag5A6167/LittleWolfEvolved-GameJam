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

        self._update_surface()

    def _update_surface(self):
     
        self.surface = self.font.render(self.text_content, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.screenWidth // 2, self.screenHeight // 2 - 100)
        self.rect.x += 1
    def draw(self, surface):
       
        surface.blit(self.surface, self.rect)