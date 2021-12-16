import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaToinenReitti(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-kakola.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_39"

        # create exits
        self.exit_a = "scene_36"
        self.exit_b = "scene_40"
        self.exit_c = "scene_39"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kävelet ympäri rakennusta yrittäen löytää sisäänpääsyä, mutta turhaan. "
                       "Ainoa sisäänpääsy vaikuttaisi olevan tikkaat avoinna olevaan ikkunaan. "
                       "<br><br>"
                       "Huomaat rakennuksen pihalla myös kivan näköisen tekolammen täynnä mulkoilevia "
                       "kaloja. Mitä teet?"
                       "<br><br><br>"
                       "        A) <b>Tikkaat</b>                               B) <b>Lampi</b>"
                       )
        return description
