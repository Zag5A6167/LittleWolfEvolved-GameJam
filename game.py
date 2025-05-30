import  pygame 
import os
from wolf import Wolf
class Game:
    def __init__(self,screen_width,screen_height,caption):
       self.screen_width = screen_width
       self.screen_height = screen_height

       self.screen_width_center = screen_width // 2
       self.screen_height_center = screen_height // 2
       self.screen = pygame.display.set_mode((screen_width,screen_height))
       pygame.display.set_caption(caption)


       self.running = True
       self.clock = pygame.time.Clock()
       self.FPS = 60

       self.all_sprites = pygame.sprite.Group()
       
       #####create   wolf ####
       self.wolf  = Wolf(self.screen_width_center,self.screen_height_center)
       self.all_sprites.add(self.wolf)
       
      
    

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.screen.fill((255,255,0))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()
    def update(self):
        self.all_sprites.update()


    def run(self):
        while self.running:
            self.handle_event()
            self.update()
            self.draw()
        pygame.quit()
