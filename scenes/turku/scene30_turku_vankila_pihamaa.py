import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaPihamaa(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-kakola.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_30"

        # create exits
        self.exit_a = "scene_31"
        self.exit_b = "scene_34"
        self.exit_c = "scene_35"

        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kävelet pitkin rakennuksen pihaa.<br> "
                       "Pian katseesi osuu kiveen, johon on piirretty nuoli. Nuoli osoittaa "
                       "maahan kiven vieressä."
                       "<br><br>"
                       "Huomaat rakennuksen seinustalla lapion ja ajattelet, että kaivat sillä nuolen "
                       "osoittamasta paikasta. Toisaalta nuoli voi tarkoittaa mitä vain, pitäisikö etsiä "
                       "vielä muualta. Vai pitäisikö pyrkiä rakennukseen sisään?"
                       "<br><br><br><br><br>"
                       "        A) <b>Lapio</b>                                 B) <b>Muualta</b>                               C) <b>Rakennus</b>"
                       )
        return description
