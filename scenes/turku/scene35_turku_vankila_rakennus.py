import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaRakennus(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-kakola.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_35"

        # create exits
        self.exit_a = "scene_36"
        self.exit_b = "scene_39"
        self.exit_c = "scene_30"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kierrät pihalla rakennusta ja yrität löytää sisäänpääsyä vanhaan "
                       "vankilarakennukseen. Huomaat seinustalla katonrajassa avonaisen ikkunan "
                       "noin 5 metrin korkeudessa. Niiden alapuolella on ränsistyneessä kunnossa "
                       "olevat palotikkaat, ehkä niitä pitkin voisi kiivetä. "
                       "<br><br>"
                       "Otatko riskin niiden kestävyydestä vai etsitkö vaihtoehtoista reittiä sisään?"
                       "Se voisi mahdollisesti löytyä myös pihamaalta.. "
                       "<br><br><br><br><br>"
                       "        A) <b>Tikkaat</b>                             B) <b>Toinen reitti</b>                         C) <b>Pihamaa</b>"
                       )
        return description
