import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaPihamaaLapioPois(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-kakola.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_33"

        # create exits
        self.exit_a = "scene_101"
        self.exit_b = "scene_101"
        self.exit_c = "scene_101"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Jänistät luolaan menosta ja päätät lähteä etsimään aarretta muualta. "
                       "Kävelen luolan ohi kohti läheistä metsää. Liukastut kuitenkin "
                       "liukkaaseen sammaleeseen kalliolla ja loukkaat nilkkasi kaatuessasi. "
                       "<br><br>"
                       "Ambulanssi noutaa sinut hetken kuluttua läheiseen sairaalaan ja aarrejahti"
                       "saa ikävän lopun."
                       "<br><br><br>"
                       "<b>HÄVISIT PELIN</b>"
                       )
        return description
