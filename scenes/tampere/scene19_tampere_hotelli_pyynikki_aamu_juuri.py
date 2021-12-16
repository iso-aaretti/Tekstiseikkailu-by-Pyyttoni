import pygame
from scenes.scene import Scene, GameObject


class SceneTampereHotelliPyynikkiAamuJuuri(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-juuri.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_19"

        # create exits
        self.exit_a = "scene_101"
        self.exit_b = "scene_19"
        self.exit_c = "scene_19"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kiertelet hetken tornin juurta tarkkaavaisena. Hetken pyörittyäsi huomaat "
                       "kauhuksesi maassa kohdan, josta on selvästi kaivettu viimeyönä. Kun "
                       "siirrät multaa pois tieltä huomaat, että onkalossa on tyhjä arkku. Joku "
                       "ehti nopeammin apajille! Olet perinkotaisin pettynyt ja palaat seuraavalla "
                       "junalla Helsinkiin. "
                       "<br><br>"
                       "<b>HÄVISIT PELIN</b>"
                       )
        return description
