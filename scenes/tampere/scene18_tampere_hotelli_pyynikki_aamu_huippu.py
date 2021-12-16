import pygame
from scenes.scene import Scene, GameObject


class SceneTampereHotelliPyynikkiAamuHuippu(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-ylhaalla.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_18"

        # create exits
        self.exit_a = "scene_3"
        self.exit_b = "scene_19"
        self.exit_c = "scene_18"
        
        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Kiipeät Pyynikin Näköistornin huipulle ja olet hengästynyt. "
                       "Nopeasti kuitenkin huomaat edessä avautuvat kauniit maisemat ja "
                       "et voi kuin ihailla niitä. <br><br> Alat tutkiskella tornin huippua ja "
                       "huomaat pian seinään raapustetun tekstin. Siinä lukee yksi sana, "
                       "'TURKU'. Liittyykö sana aarrejahtiin? Lähdetkö Turkuun vai "
                       "jätätkö tekstin huomioitta ja siirryt etsimään tornin juutelta?"
                       "<br><br><br><br><br><br>"
                       ""
                       "        A) <b>Turku</b>                                   B) <b>Juuri</b>"
                       )
        return description
