import pygame
from scenes.scene import Scene, GameObject


class SceneTampereHotelliPyynikkiAamu(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-juuri.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_12"

        # create exits
        self.exit_a = "scene_18"
        self.exit_b = "scene_19"
        self.exit_c = "scene_12"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Saavut Pyynikin Näkötornille aikaisin aamulla, linnut laulavat syksyistä sointuaan. "
                       "Tuunnet olosi reippaaksi ja valmiiksi etsimään aarretta. Mistä aloittaisit etsinnät?"
                       "<br><br> "
                       "Huipulta vai juuresta?"
                       "<br><br><br><br>"
                       "<br><br><br><br>"
                       "        A) <b>Huippu</b>                                    B) <b>Juuri</b>"
                       )
        return description
