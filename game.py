import  pygame 
import os
import random
from wolf import Wolf
from button import Button
from item_data import ALL_GAME_ITEMS,POSSIBLE_ITEM_NAMES,ITEM_WEIGHTS
from textItemShow import TextShowRandomItem
class Game:
    def __init__(self,screen_width,screen_height,caption):
       self.screen_width = screen_width
       self.screen_height = screen_height

       self.screen_width_center = screen_width // 2
       self.screen_height_center = screen_height // 2
       self.screen = pygame.display.set_mode((screen_width,screen_height))
       pygame.display.set_caption(caption)

       self.background = pygame.image.load(os.path.join("asset", "background", "background_main.png")).convert_alpha()


       self.button_font_size = 32
       self.menu_button_font = pygame.font.Font(None, self.button_font_size) 
       self.buttons = []


       self.setup_menu_btn()

       self.running = True
       self.clock = pygame.time.Clock()
       self.FPS = 60

       self.all_sprites = pygame.sprite.Group()

       
       #####create   wolf ####
       self.wolf  = Wolf(self.screen_width_center,self.screen_height_center)
       self.all_sprites.add(self.wolf)
       
      
        ### item data ###
       self.all_game_items_data = ALL_GAME_ITEMS
       self.possible_item_names = POSSIBLE_ITEM_NAMES
       self.item_weights = ITEM_WEIGHTS

        
       self.item_display_text = None 


    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            for button in self.buttons:
                button.handle_event(event)

    def draw(self):
        # self.screen.fill((255,255,0))
        self.screen.blit(self.background,(0,0))
        self.all_sprites.draw(self.screen)
        self.wolf.draw_health_bar(self.screen,self.screen_width)

        if self.item_display_text:
            self.item_display_text.draw(self.screen)
        for button in self.buttons:
            button.draw(self.screen)


        pygame.display.flip()
    def update(self):
        self.all_sprites.update()


    def run(self):
        while self.running:
            self.handle_event()
            self.update()
            self.draw()
        pygame.quit()


    def setup_menu_btn(self):
        buttonWidth = 200
        buttonHeight = 80
        padding = 50
      


        #### Go hunting ######
        self.goHuntingButton = Button(padding,padding,buttonWidth,buttonHeight,"Go Hunting",self.menu_button_font,action=self._goHuntingButton,color=(255,255,255),hover_color=(255,0,200)
                             )
        self.buttons.append(self.goHuntingButton)
      

        ### Go bed #####
        goBedButton_y = padding + buttonHeight + padding
        self.goBedButton = Button(padding,goBedButton_y,buttonWidth,buttonHeight,"Go Bed",self.menu_button_font,action=self._goBedButton,color=(255,255,255),hover_color=(255,0,200)
                             )
        self.buttons.append(self.goBedButton)


    def _goHuntingButton(self):
        chosen_item_name = random.choices(self.possible_item_names, weights=self.item_weights, k=1)[0]
       


        chosen_item_data = next((item for item in self.all_game_items_data if item["name"] == chosen_item_name), None)

       


        if chosen_item_data:

            item_message = f"Found: {chosen_item_data['name']}!. {chosen_item_data.get('description', 'No description available.')}"
            print(item_message)
           
            self.item_display_text = TextShowRandomItem(
                item_message,
                screenWidth=self.screen_width,
                screenHeight=self.screen_height,
                color=(255, 255, 255) 
            )
            


            # print(f"Your found[{chosen_item_data['name']}]!")
    
            # print(f"Description: {chosen_item_data.get('description', 'No description available.')}")

            effect_type = chosen_item_data.get("effect_type")
            effect_value = chosen_item_data.get("effect_value", 0) 
            damage_amount =chosen_item_data.get('damage_amout',0)
            if effect_type == "none":
                pass
            
            elif effect_type == "fall_and_damage":
                self.wolf.takeDamage(damage_amount)
            else:
                print(f"Item '{chosen_item_data['name']}' has an unsupported effect type: {effect_type}.")
        else:
            print(f"Error: Could not find data for item '{chosen_item_name}'.")
        # -----------------------------------------------------

    def _goBedButton(self):
        print("press")
