import pygame
class Button:
    def __init__(self, x, y, width, height, text, font_object, action=None,
                 color=(200, 200, 200), hover_color=(220, 220, 220), text_color=(0, 0, 0)):
       
      
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

        self.font = font_object

        
        self.action = action

        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color

    def draw(self, surface):
      
        mouse_pos = pygame.mouse.get_pos()

        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, current_color, self.rect)

        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()



    