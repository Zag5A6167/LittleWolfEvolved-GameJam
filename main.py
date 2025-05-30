from game import Game
import pygame 



screen_width = 1280     
screen_height = 720 
caption = "Little Wolf Growing "


if __name__ == "__main__":
    pygame.init() 
    pygame.font.init()
    game = Game(screen_width,screen_height,caption)
    game.run()