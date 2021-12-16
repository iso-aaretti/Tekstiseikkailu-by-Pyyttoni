import pygame
from scenes.scene import Scene, GameObject

# Tampere pyynikki Yö
class SceneTampereHotelliPyynikkiYoKaivaAvaimet(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/tre-pyynikin-nakotorni-juuri-yo.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_16"

        # create exits
        self.exit_a = "scene_6"
        self.exit_b = "scene_9"
        self.exit_c = "scene_16"
        
        # propeller fate
        self.b_discovered_propeller_fate = False

    def get_description(self, player):
        description = ("Vartija raapii hetken päätään ja toteaa sitte, että 'selvä'."
                       "Hän tarjoutuu auttamaan sinua avainten etsinnässä. Avaimia "
                       "ei luonnollisestikaan löydy. Hetken esitettyäsi, että avaimet "
                       "olisivat oikeasti hukassa sanot vartijalle, että 'Pärjään kyllä "
                       "ilmankin'. Teet seuraavaa:"
                       "<br><br><br><br>"
                       "        A) <b>Hotelliin</b>                                   B) <b>Piiloudu</b>"
                       )
        return description
