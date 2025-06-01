
import pygame

class GameOverScreen:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen_width_center = screen_width // 2
        self.screen_height_center = screen_height // 2
    
        self.game_over_font = pygame.font.Font(None, 100) 
        self.restart_font = pygame.font.Font(None, 40) 

     
        self.text_color_game_over = (255, 0, 0) 
        self.text_color_restart = (255, 255, 255) 
        self.background_color = (0, 0, 0) 

    def draw(self, screen):

        screen.fill(self.background_color)


        game_over_text_surface = self.game_over_font.render("GAME OVER", True, self.text_color_game_over)
        game_over_text_rect = game_over_text_surface.get_rect(
            center=(self.screen_width_center, self.screen_height_center - 50)
        )
        screen.blit(game_over_text_surface, game_over_text_rect)

    
        restart_text_surface = self.restart_font.render("Press 'R' to Restart", True, self.text_color_restart)
        restart_text_rect = restart_text_surface.get_rect(
            center=(self.screen_width_center, self.screen_height_center + 50)
        )
        screen.blit(restart_text_surface, restart_text_rect)

   