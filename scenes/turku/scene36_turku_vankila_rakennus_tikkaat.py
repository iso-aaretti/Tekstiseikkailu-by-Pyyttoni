import pygame
from scenes.scene import Scene, GameObject


class SceneTurkuVankilaRakennusTikkaat(Scene):
    
    def __init__(self):
        super().__init__()

        self.background = pygame.Surface((640, 480))
        self.background = pygame.image.load("scenes/image/turku-kakola.jpg")
        self.background = self.background.convert()

        self.text_colour = pygame.Color("#141414")
        self.background_colour = pygame.Color("#F0F0F0")

        # set id
        self.id = "scene_36"

        # create exits
        self.exit_a = "scene_37"
        self.exit_b = "scene_30"
        self.exit_c = "scene_36"

        # propeller fate
        self.b_discovered_propeller_fate = False


    def get_description(self, player):
        description = ("Lähdet varovaisesti kipuamaan tikkaita pitkin kohti avonaista ikkunaa. "
                       "Etenet askel askelmalta hitaasti ja keskittyneesti. Et ehdi huomatakkaan, "
                       "kuinka yhtäkkinen raju tuulenpuuska tarttuu takkiisi ja otteesi lipeää. "
                       "<br><br>"
                       "Tipahdat maahan selällesi ja kuuluu raksahdus. Onneksi olit kerinnyt kiipeämään "
                       "vasta reilun metrin verran ja raksahduskin paljastui alleesi jääneen oksan "
                       "aiheuttamaksi. Yritätkö uudelleen vai siirrytkö etsimään pihamaalta?"
                       "<br><br><br><br><br>"
                       "        A) <b>Uudestaan</b>                              B) <b>Pihamaa</b>"
                       )
        return description
